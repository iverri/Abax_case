import paho.mqtt.client as mqtt
from createTables import createTables, dropTables
from mqttClient import on_connect, on_message

mqttClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("mqtt.hsl.fi", 1883, 60)

seeData = input("See data? (y/n)")
if seeData == "y":
    from constants import con

    cur = con.cursor()
    cur.execute("SELECT * FROM messagePayloads")
    rows = cur.fetchall()
    for row in rows:
        print(row)

response = input("Reset database? (y/n)")
if response == "y":
    dropTables()

createTables()


mqttClient.loop_start()

while True:
    action = input(
        """What would you like to do?
Show buses close to me (Type: 1)
Show all buses (Type: 2)
Type q to quit
                   
"""
    )
    if action == "1":
        response = input(
            """What is your current location? 
Available locations:
    City Centre (1)
    Kallio (2)
    Toolo (3)
    Eira (4)
    Lauttasaari (5)
    Hakaniemmi (6)
    Kurvi (7)
    Hermanni (8)
    Pasila (9)     
    Toukola (10)
    Haaga (11)
    Munkkiniemi (12)
    Kuusisaari (13)         
"""
        )
