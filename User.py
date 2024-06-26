class User:
    def __init__(self, username, password):
        self.name = "giovi"
        self.surname = "desio"
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.username

    def get_name(self):
        if self.name is not None:
            return self.name
        else:
            return None

    def get_surname(self):
        if self.surname is not None:
            return self.surname
        else:
            return None

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password
        }
