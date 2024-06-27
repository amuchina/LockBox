class User:
    def __init__(self, username, password):
        self.name = "giovi"
        self.surname = "desio"
        self.username = username  # username may be also email
        self.password = password

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

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
