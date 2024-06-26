import random


def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


class Locker:
    def __init__(self, service_name, username, password):
        self.service_name = service_name
        self.username = username
        self.password = password
        self.bg_color = generate_random_color()

    def __repr__(self):
        return f"Locker(service_name='{self.service_name}', username='{self.username}', password='******')"

    def to_tuple(self):
        return (self.service_name, self.username, self.password)

