import sqlite3 as sql

class Sql():
    def __init__(self, databaseName = "test.db", tableName = "users"):
        self.databaseName = databaseName
        self.tableName = tableName 
        self.db = sql.connect(databaseName)
        self.cr = self.db.cursor()

    def select(self, select = "*", where = ""):

        if where == "":
            self.cr.execute(f"SELECT {select} FROM {self.tableName} {where}")

        else:
            self.cr.execute(f"SELECT {select} FROM {self.tableName} WHERE {where}")

        return self.cr.fetchall()


    def insert(self, column = "", value = ""):
        if column == "":
            self.code = f"INSERT INTO {self.tableName} VALUES {str(value)}"

        else:
            self.code = f"INSERT INTO {self.tableName} ({column}) VALUES {str(value)}"


        self.cr.execute(self.code)
        self.db.commit()

    def delete(self, delete, where):
        self.code = f"DELETE FROM {self.tableName} WHERE {delete} = '{where}'"
        self.cr.execute(self.code)
        self.db.commit()

    
    def update(self, SET, WHERE):
        self.code = f"UPDATE {self.tableName} SET {SET} WHERE {WHERE}"
        self.cr.execute(self.code)
        self.db.commit()


