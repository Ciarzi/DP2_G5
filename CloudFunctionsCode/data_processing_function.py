import mysql.connector
import json
import base64

connection = mysql.connector.connect(host='35.187.114.126',
                                     database='lestsprayDb',
                                     user='root',
                                     password='datapdb2')

sql_insert_sensor_input = """INSERT INTO sensorsInput (sensorId, soilHumidity, relativeHumidity, temperature, date) VALUES (%s,%s,%s,%s,%s)"""


def data_process(event, context):
    data = base64.b64decode(event['data']).decode('utf-8')
    sensor = json.loads(data)
    cursor = connection.cursor(buffered=True)
    insert_tuple = (sensor["id"],sensor["soilHumidity"],sensor["relativeHumidity"],sensor["temperature"],sensor["date"])
    cursor.execute(sql_insert_sensor_input, insert_tuple)
    connection.commit()
