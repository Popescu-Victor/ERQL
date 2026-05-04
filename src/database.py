import sqlite3
import errors_messagebox

class DataBase:
    def __init__(self, sqlite):
        self.conn = sqlite3.connect(sqlite)
        self.cursor = self.conn.cursor()