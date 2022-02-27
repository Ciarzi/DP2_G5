import random
from datetime import datetime
import time
import mysql.connector


connection = mysql.connector.connect(host='192.168.1.141',
                                     database='LetsprayDB',
                                     user='root',
                                     password='ZurichDb')

SENSORS_TOTAL = 100
sql_get_last_sensor_input = """SELECT sensorId,
    soilHumidity,
    relativeHumidity,
    temperature,
    date FROM sensorsInput WHERE sensorId =%s ORDER BY sensorsInputId DESC LIMIT 1"""

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
        sensor["soilHumidity"] = random.randint(
            max(records[0]["soilHumidity"]-10, 0), min(records[0]["soilHumidity"]+10, 100))
        sensor["relativeHumidity"] = random.randint(max(
            records[0]["relativeHumidity"]-10, 0), min(records[0]["relativeHumidity"]+10, 100))
        sensor["temperature"] = round(random.uniform(
            max(records[0]["temperature"]-5, -2), min(records[0]["temperature"]+5, 40)),1)
        sensor["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(sensor)
    time.sleep(1)