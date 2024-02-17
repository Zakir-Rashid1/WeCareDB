# Module to connect to MySQL database

import mysql.connector
from database.config import DATABASE_CONFIG

class DBConnector:
    def __init__(self):
        self.config = DATABASE_CONFIG

    def connect(self):
        return mysql.connector.connect(**self.config)
    
    def close(self, conn):
        conn.close()