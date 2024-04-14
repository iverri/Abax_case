from constants import con


def createTables():
    cur = con.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS messagePayloads (
        BusID INTEGER PRIMARY KEY,
        Route TEXT NOT NULL,
        Direction TEXT NOT NULL,
        Latitude REAL NOT NULL,
        Longitude REAL NOT NULL,
        LastUpdate TEXT NOT NULL,
        LastStop INTEGER
);
    """
    )
    con.commit()


def dropTables():
    cur = con.cursor()
    cur.execute(
        """
    DROP TABLE IF EXISTS messagePayloads;
    """
    )
    con.commit()
