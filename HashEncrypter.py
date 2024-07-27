import bcrypt
import hashlib
import mysql.connector
import LockBoxDBManager
import Auth
import binascii


class HashEncrypter:
    def __init__(self):
        print("HashEncrypter initialized")

    def gen_sha256_digest(self, salt, password):
        byte_digest = hashlib.pbkdf2_hmac(hash_name='sha512', password=password, salt=salt, iterations=250000)
        hex_digest = binascii.hexlify(byte_digest)
        return hex_digest

    def generate_salt(self, authenticator: Auth, dbcontroller: LockBoxDBManager):
        checksaltquery = """
            SELECT personal_user_salt
            FROM lockbox.users
            WHERE username = %s
            AND password = %s;
        """
        try:
            with dbcontroller.get_cursor() as cursor:
                cursor.execute(checksaltquery, (authenticator.get_authenticated_username(), authenticator.get_authenticated_password()))
                response = cursor.fetchall()
                bytesalt = bcrypt.gensalt()
                stringsalt = bytesalt.decode('utf-8')
                updateusersaltquery = """
                    UPDATE lockbox.users
                    SET personal_user_salt = %s
                    WHERE username = %s; 
                """
                cursor.execute(updateusersaltquery, (stringsalt, authenticator.get_authenticated_username()))
                dbcontroller.conn.commit()
                print(f"Successfully initialized salt {stringsalt} for user: {authenticator.get_authenticated_username(), authenticator.get_authenticated_password()}")
                return stringsalt, bytesalt
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False




