from constants import con
import json


def on_connect(client, userdata, flags, rc, properties=None):
    client.subscribe("/hfp/v2/journey/ongoing/vp/bus/+/+/+/+/+/+/+/2/#")
    client.subscribe("/hfp/v2/journey/ongoing/dep/bus/+/+/+/+/+/+/+/+/#")
    client.subscribe("/hfp/v2/journey/ongoing/vjout/bus/+/+/+/+/+/+/+/+/#")


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))

    if "VP" in payload:
        data = payload["VP"]
        busID = data["veh"]
        route = data["desi"]
        direction = data["dir"]
        latitude = data["lat"]
        longitude = data["long"]
        last_update = data["tst"]
        if checkIfBusExists(busID):
            cur = con.cursor()
            cur.execute(
                "UPDATE messagePayloads SET Route = ?, Direction = ?, Latitude = ?, Longitude = ?, LastUpdate = ? WHERE BusID = ?",
                (route, direction, latitude, longitude, last_update, busID),
            )
            con.commit()
        else:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO messagePayloads (BusID, Route, Direction, Latitude, Longitude, LastUpdate) VALUES (?, ?, ?, ?, ?, ?)",
                (busID, route, direction, latitude, longitude, last_update),
            )
            con.commit()

    if "DEP" in payload:
        data = payload["DEP"]
        busID = data["veh"]
        route = data["desi"]
        direction = data["dir"]
        latitude = data["lat"]
        longitude = data["long"]
        last_update = data["tst"]
        last_stop = data["stop"]
        if checkIfBusExists(busID):
            cur = con.cursor()
            cur.execute(
                "UPDATE messagePayloads SET Route = ?, Direction = ?, Latitude = ?, Longitude = ?, LastUpdate = ?, LastStop = ? WHERE BusID = ?",
                (route, direction, latitude, longitude, last_update, last_stop, busID),
            )
            con.commit()
        else:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO messagePayloads (BusID, Route, Direction, Latitude, Longitude, LastUpdate, LastStop) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (busID, route, direction, latitude, longitude, last_update, last_stop),
            )
            con.commit()

    if "VJOUT" in payload:
        busID = payload["VJOUT"]["veh"]
        if checkIfBusExists(busID):
            cur = con.cursor()
            cur.execute("DELETE FROM messagePayloads WHERE BusID = ?", (busID,))
            con.commit()


def checkIfBusExists(busID):
    cur = con.cursor()
    cur.execute("SELECT * FROM messagePayloads WHERE BusID = ?", (busID,))
    bus = cur.fetchone()
    if bus:
        return True
    return False
