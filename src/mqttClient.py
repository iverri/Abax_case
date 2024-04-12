from constants import con


def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    client.subscribe("/lahellasi/BUS/")


def on_message(client, userdata, msg):
    print("Received: " + msg.topic + " " + msg.payload)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO messagePayloads (message, payload) VALUES (?, ?)",
        (msg.topic, msg.payload),
    )
