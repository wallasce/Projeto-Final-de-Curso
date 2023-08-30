import sqlite3

class SQLiteManager:
    def __init__(self, database : str) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def stopConnection(self) -> None:
        self.cursor.close()

    def selectDataFrom(self, table : str) -> dict:
        self.cursor.execute('''
            SELECT SourceTimestamp, Value FROM "''' + table + '''";
        ''')

        return self.cursor.fetchall()