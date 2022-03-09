import mysql.connector
import json
import base64
#import time
#import adafruit_dht
#import psutil
#import RPi.GPIO as GPIO
import os
from google.cloud import pubsub_v1

connection = mysql.connector.connect(host='35.187.114.126',
                                     database='lestsprayDb',
                                     user='root',
                                     password='datapdb2')

sql_insert_sensor_input = """INSERT INTO sensorsInput (sensorId, soilHumidity, relativeHumidity, temperature, date) VALUES (%s,%s,%s,%s,%s)"""

sql_get_data_custom_sensor = """SELECT sensorId, 
                             squareMeter, 
                             soilHumidity, 
                             grass, 
                             flowerPreference, 
                             timePreference 
                             FROM userSensorConfig
                             WHERE sensorId = %s"""

sql_get_data_sensor = """SELECT sensorId, soilHumidity,relativeHumidity, temperature, date
FROM sensorsInput where sensorId=%s order by date desc limit 1;"""


type_watering = ["Abundante", "Medio", "Ecológico"]

# timePreference realmente es el Tipo de regado

LED_PIN = 13
LED_PIN_2 = 21


def data_process(event, context):
    data = base64.b64decode(event['data']).decode('utf-8')
    sensor = json.loads(data)
    cursor = connection.cursor(buffered=True)
    insert_tuple = (sensor["id"], sensor["soilHumidity"],
                    sensor["relativeHumidity"], sensor["temperature"], sensor["date"])
    cursor.execute(sql_insert_sensor_input, insert_tuple)
    connection.commit()

    sensorId = (sensor["id"],)
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_get_data_custom_sensor, sensorId)
    records = cursor.fetchall()
    sensor_custom = {}
    if records is None or len(records) < 1:
        sensor_custom["sensorId"] = sensorId
        sensor_custom["squareMeter"] = None
        sensor_custom["soilHumidity"] = 40
        sensor_custom["grass"] = None
        sensor_custom["flowerPreference"] = None
        sensor_custom["timePreference"] = None
    else:
        sensor_custom["sensorId"] = records[0][0]
        sensor_custom["squareMeter"] = records[0][1]
        sensor_custom["soilHumidity"] = records[0][2]
        sensor_custom["grass"] = records[0][3]
        sensor_custom["flowerPreference"] = records[0][4]
        sensor_custom["timePreference"] = records[0][5]

    cursor.close()

    cursor = connection.cursor(buffered=True)
    cursor.execute(sql_get_data_sensor, sensorId)
    records = cursor.fetchall()
    sensor_data = {}
    if len(records) >= 1:
        sensor_data["sensorId"] = records[0][0]
        sensor_data["soilHumidity"] = records[0][1]
        sensor_data["relativeHumidity"] = records[0][2]
        sensor_data["temperature"] = records[0][3]
        sensor_data["date"] = records[0][4]
    cursor.close()

    # comparar humedad que llega del sensor con la parametrizada:

    # humedad del suelo del sensor es menor  que la del custom
    if sensor_data["soilHumidity"] < sensor_custom["soilHumidity"]:
        # ¿tiene prametrizada una preferencia de regado?:
        if sensor_custom["timePreference"] is not None:
            value_watering = sensor_custom["timePreference"]
            if value_watering == type_watering[0]:
                print("Regando en modo Ecológico")

                # try:
                #     GPIO.setmode(GPIO.BCM)
                #     GPIO.setup(LED_PIN_2, GPIO.OUT)
                #     GPIO.output(LED_PIN_2, GPIO.HIGH)
                #     time.sleep(1)
                #     GPIO.output(LED_PIN_2, GPIO.LOW)
                #     GPIO.cleanup()

                # except RuntimeError as error:
                #     print(error.args[0])
                #     time.sleep(2.0)
                # except Exception as error:
                #     sensor.exit()
                #     raise error

            elif value_watering == type_watering[1]:
                print("Regando en modo Medio")

            #     try:
            #         GPIO.setmode(GPIO.BCM)
            #         GPIO.setup(LED_PIN, GPIO.OUT)
            #         GPIO.output(LED_PIN, GPIO.HIGH)
            #         time.sleep(1)
            #         GPIO.output(LED_PIN, GPIO.LOW)
            #         GPIO.cleanup()

            #     except RuntimeError as error:
            #         print(error.args[0])
            #         time.sleep(2.0)
            #     except Exception as error:
            #         sensor.exit()
            #         raise error

            elif value_watering == type_watering[2]:
                print("Regando en modo Abundante")

                # try:
                #     GPIO.setmode(GPIO.BCM)
                #     GPIO.setup(LED_PIN, GPIO.OUT)
                #     GPIO.output(LED_PIN, GPIO.HIGH)
                #     time.sleep(1)
                #     GPIO.output(LED_PIN, GPIO.LOW)
                #     GPIO.cleanup()
                #     GPIO.setmode(GPIO.BCM)
                #     GPIO.setup(LED_PIN_2, GPIO.OUT)
                #     GPIO.output(LED_PIN_2, GPIO.HIGH)
                #     time.sleep(1)
                #     GPIO.output(LED_PIN_2, GPIO.LOW)
                #     GPIO.cleanup()

                # except RuntimeError as error:
                #     print(error.args[0])
                #     time.sleep(2.0) 
                # except Exception as error:
                #     sensor.exit()
                #     raise error
        else:
            dif_humidity = sensor_custom["soilHumidity"] - \
                sensor_data["soilHumidity"]
            if (dif_humidity >= 10 and sensor_data["temperature"] > 25):
                print("Regando en modo Ecológico")
            else:
                print('No hay riego')

        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=os.getenv('SENSOR_PROJECT_ID'),
            topic='raspberry_trigger'
        )

        future = publisher.publish(topic_name, ("{\"message\": \"hello\"}").encode('utf-8'), sender='datagen_cloud_function')
        future.result()
