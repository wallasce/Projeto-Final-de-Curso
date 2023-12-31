import sqlite3

class SQLiteManager:
    def __init__(self, database : str) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def stopConnection(self) -> None:
        self.cursor.close()

    def clearData(self) -> None:
        for table in self.selectTablesInformations():
            self.cursor.execute('''
                DROP TABLE IF EXISTS "''' + table[2] + '''";
            ''')

    def selectDataFrom(self, table : str) -> dict:
        self.cursor.execute('''
            SELECT SourceTimestamp, Value FROM "''' + table + '''";
        ''')

        return self.cursor.fetchall()
    
    def selectTablesInformations(self) -> dict:
        self.cursor.execute('''
            SELECT * FROM sqlite_master WHERE type='table';
        ''')

        return self.cursor.fetchall()