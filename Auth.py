import User
import mysql.connector
import LockBoxDBManager


class Auth:
    def __init__(self):
        self.authenticated_user = None
        print(f"Authenticator initialized: current user({self.authenticated_user})")

    def register(self, newuser: User, dbcontroller: LockBoxDBManager):
        query = """
            INSERT INTO lockbox.users (name, surname, username, password) 
            VALUES (%s, %s, %s, %s);
        """
        try:
            dbcontroller.get_cursor().execute(query, (newuser.get_name(), newuser.get_surname(), newuser.get_username(), newuser.get_password()))
            dbcontroller.conn.commit()
            print(f"Successfully created user: {newuser.get_name(), newuser.get_surname(), newuser.get_username(), newuser.get_password()}")
            loginrequest = self.login(newuser, dbcontroller)
            if loginrequest:
                self.authenticated_user = loginrequest
                return True
            else:
                print("Not logged in")
                return False
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

    def logout(self):
        self.authenticated_user = None

    def updateuserinfo(self, updatedname, updatedsurname, updatedusername, updatedpassword, dbcontroller: LockBoxDBManager):
        updatenamequery = """
            UPDATE lockbox.users
            SET name = %s
            WHERE username = %s;
        """
        updatesurnamequery = """
            UPDATE lockbox.users
            SET surname = %s
            WHERE username = %s;
        """
        updateusernamequery = """
            UPDATE lockbox.users
            SET username = %s
            WHERE username = %s; 
        """
        updatepasswordquery = """
            UPDATE lockbox.users
            SET password = %s
            WHERE username = %s; 
        """
        try:
            with dbcontroller.get_cursor() as cursor:
                if updatedname is not None:
                    cursor.execute(updatenamequery, (updatedname, self.authenticated_user[3]))
                    dbcontroller.conn.commit()
                    print("Name successfully updated")
                    return True
                if updatedsurname is not None:
                    cursor.execute(updatesurnamequery, (updatedsurname, self.authenticated_user[3]))
                    dbcontroller.conn.commit()
                    print("Surname successfully updated")
                    return True
                if updatedusername is not None:
                    cursor.execute(updateusernamequery, (updatedusername, self.authenticated_user[3]))
                    dbcontroller.conn.commit()
                    print("Username successfully updated")
                    return True
                if updatedpassword is not None:
                    cursor.execute(updatepasswordquery, (updatedpassword, self.authenticated_user[3]))
                    dbcontroller.conn.commit()
                    print("Password successfully updated")
                    return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def get_authenticated_user(self):
        return self.authenticated_user

    def get_authenticated_user_id(self):
        return self.authenticated_user[0]

    def get_authenticated_username(self):
        return self.authenticated_user[3]

    def get_authenticated_password(self):
        return self.authenticated_user[4]

    def get_authenticated_user_to_dict(self):
        return {
            "id": self.authenticated_user[0],
            "name": self.authenticated_user[1],
            "surname": self.authenticated_user[2],
            "username": self.authenticated_user[3],
            "password": self.authenticated_user[4],
            "locker_count": self.authenticated_user[5]
        }
