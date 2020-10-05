from random import randint


class Bot:
    def __init__(self, name):
        self.tname = f"Bot {name}"
        self.name = f"\033[1;30mBot\033[0m {name}"
        self.choice = randint(0, 2)

    def output(self):
        print(f"{self.name} enter choice... {self.choice}")
