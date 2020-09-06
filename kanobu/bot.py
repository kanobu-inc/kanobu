from random import randint


class Bot:
    def __init__(self, name):
        self.name = name
        self.choice = randint(1, 3)

        print(f"{self.name} enter choice... {self.choice - 1}")
