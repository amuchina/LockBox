import random
import HashEncrypter
import cryptography

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


class Locker:
    def __init__(self, service_name, username, password):
        self.service_name = service_name
        self.username = username
        self.password = password
        self.bg_color = generate_random_color()

    def save(self, hashencrypter: HashEncrypter, salt):
        encrypted_password_data = hashencrypter.gen_sha256_digest(salt=salt, password=self.password)  # this only goes to db, it is not the encrypted password

    def to_string(self):
        return f"Locker(service_name='{self.service_name}', username='{self.username}', password='{self.password}')"

    def to_tuple(self):
        return (self.service_name, self.username, self.password)

