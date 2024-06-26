import mysql.connector

class LockBoxDBManager:
    def __init__(self):
        self.conn = None
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password"
            )
            print("Connection established")
        except mysql.connector.Error as err:
            print(f"Connection failed: {err}")

    def get_cursor(self):
        if self.conn and self.conn.is_connected():
            return self.conn.cursor()
        else:
            raise mysql.connector.Error("Connection is not established or has been closed.")

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connection closed")
