import User
import mysql.connector
import LockBoxDBManager


class Auth:
    def __init__(self):
        self.authenticated_user = None

    def register(self, newuser: User, dbcontroller: LockBoxDBManager):
        query = """
            INSERT INTO lockbox.users (name, surname, username, password) 
            VALUES (%s, %s, %s, %s);
        """
        try:
            dbcontroller.get_cursor().execute(query, (newuser.get_name(), newuser.get_surname(), newuser.get_username(), newuser.get_password()))
            dbcontroller.conn.commit()
            print("User created successfully")  # check if user already exists with same username/email
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            dbcontroller.get_cursor().close()

    def login(self, user: User, dbcontroller: LockBoxDBManager):
        query = """
            SELECT * 
            FROM lockbox.users 
            WHERE username = %s 
            AND password = %s;
        """
        try:
            with dbcontroller.get_cursor() as cursor:
                cursor.execute(query, (user.get_username(), user.get_password()))
                response = cursor.fetchall()
                if response:
                    self.authenticated_user = response
                    print(f"Successfully authenticated user: {response}")
                    return True
                else:
                    print("Invalid username or password")
                    return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
