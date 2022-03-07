import random
from datetime import datetime
import mysql.connector
from google.cloud import pubsub_v1
import os
import json

connection = mysql.connector.connect(host='35.187.114.126',
                                     database='lestsprayDb',
                                     user='root',
                                     password='datapdb2')

SENSORS_TOTAL = 10
sql_get_last_sensor_input = """SELECT sensorId,
    soilHumidity,
    relativeHumidity,
    temperature,
    date FROM sensorsInput WHERE sensorId =%s ORDER BY sensorsInputId DESC LIMIT 1"""

sql_insert_sensor_input = """INSERT INTO sensorsInput (sensorId, soilHumidity, relativeHumidity, temperature, date) VALUES (%s,%s,%s,%s,%s)"""


def datagen(event, context):
    for i in range(1, SENSORS_TOTAL+1):
        sensor = {}
        sensor["id"] = i
        cursor = connection.cursor(buffered=True)
        get_data_tuple = (i,)
        cursor.execute(sql_get_last_sensor_input, get_data_tuple)
        records = cursor.fetchall()
        if records is None or len(records) < 1:
            sensor["soilHumidity"] = random.randint(0, 100)
            sensor["relativeHumidity"] = random.randint(0, 100)
            sensor["temperature"] = round(random.uniform(-2, 40),1)
            sensor["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        else:
            print(records[0])
            sensor["soilHumidity"] = random.randint(
                max(records[0][1]-10, 0), min(records[0][1]+10, 100))
            sensor["relativeHumidity"] = random.randint(max(
                records[0][2]-10, 0), min(records[0][2]+10, 100))
            sensor["temperature"] = round(random.uniform(
                max(records[0][3]-5, -2), min(records[0][3]+5, 40)),1)
            sensor["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        #insert_tuple = (i,sensor["soilHumidity"],sensor["relativeHumidity"],sensor["temperature"],sensor["date"])
        #cursor.execute(sql_insert_sensor_input, insert_tuple)
        #connection.commit()
        publisher = pubsub_v1.PublisherClient()
        topic_name = 'projects/{project_id}/topics/{topic}'.format(
            project_id=os.getenv('SENSOR_PROJECT_ID'),
            topic='sprinkler_trigger'
        )
        future = publisher.publish(topic_name,json.dumps(sensor).encode('utf-8'), sender='datagen_cloud_function')
        future.result()
