# NO TOCAR
from faker import Faker
import keyboard
import time
import random
from datetime import datetime

faker = Faker('es_ES')
USERS_TOTAL=100
users={}

def initiate_data():
    global users
    for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        user["soil_humidity"]=random.uniform(0, 100)
        user["relative_humidity"]= random.uniform(0, 100)
        user["temperature"] = random.uniform(-2, 40)
        user["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user
    return users     

# NO TOCAR

while True:
    try:  
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Exited the data generator')
            break  
        else:
            users_generated=initiate_data()
            print(users_generated)
            time.sleep(120)
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        break