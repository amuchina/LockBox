import dotenv
import mysql.connector
from dotenv import load_dotenv
import os


class LockBoxDBManager:
    def __init__(self):
        load_dotenv("envfiles/.env.secret.db")
        self.conn = None
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD")
            )
            print("Connection established")
        except mysql.connector.Error as err:
            print(f"Connection failed: {err}")


    def get_cursor(self):
        if self.conn and self.conn.is_connected():
            return self.conn.cursor(buffered=True)
        else:
            raise mysql.connector.Error("Connection is not established or has been closed.")

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connection closed")
