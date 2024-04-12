from constants import con


def createTables():
    cur = con.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS messagePayloads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message VARCHAR(255) NOT NULL,
    payload VARCHAR(255) NOT NULL
);
    """
    )
