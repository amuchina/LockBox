import User
import mysql.connector
import LockBoxDBManager

class Auth:
    def __init__(self):
        self.authenticated_user = None

    def register(self, newuser: User, dbcontroller: LockBoxDBManager):
        query = "INSERT INTO lockbox.users (name, surname, username, password) VALUES (%s, %s, %s, %s)" # syntax error
        try:
            dbcontroller.get_cursor().execute(query, newuser)
            dbcontroller.conn.commit()
            print("User created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            dbcontroller.get_cursor().close()
