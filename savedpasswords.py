import random

class SavedPassword:
    def __init__(self, service_name, username, password):
        self.service_name = service_name
        self.username = username
        self.password = password
        self.bg_color = self.generate_random_color()

    def generate_random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
