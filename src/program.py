import paho.mqtt.client as mqtt
from createTables import createTables
from mqttClient import on_connect, on_message

mqttClient = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.connect("mqtt.hsl.fi", 1883, 60)

createTables()

mqttClient.loop_forever()
