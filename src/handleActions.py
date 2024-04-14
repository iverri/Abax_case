from constants import con


def getNearbyBuses():
    cur = con.cursor()
    cur.execute("SELECT * FROM messagePayloads")
    rows = cur.fetchall()
    for row in rows:
        print(row)
