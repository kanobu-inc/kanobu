from random import randint


class Bot:
    def __init__(self, name):
        self.name = name
        self.choice = randint(0, 2)

        print(f"{self.name} enter choice... {self.choice}")
