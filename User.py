class User:
    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username  # username may be also email
        self.password = password

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

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

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password
        }
