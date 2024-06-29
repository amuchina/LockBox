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
            print(f"Successfully created and authenticated user: {newuser.get_name(), newuser.get_surname(), newuser.get_username(), newuser.get_password()}")  # check if user already exists with same username/email
            self.authenticated_user = newuser
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
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
                    self.authenticated_user = response[0]
                    print(f"Successfully authenticated user: {response[0]}")
                    return response[0]
                else:
                    print("Invalid username or password")
                    return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def get_authenticated_user(self):
        return self.authenticated_user

    def get_authenticated_user_to_dict(self):
        return {
            "id": self.authenticated_user[0],
            "name": self.authenticated_user[1],
            "surname": self.authenticated_user[2],
            "username": self.authenticated_user[3],
            "password": self.authenticated_user[4],
            "locker_count": self.authenticated_user[5]
        }
