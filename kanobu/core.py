import locale
import re

if __file__ == "__main__":
    from __init__ import __version__, __logo__
else:
    from kanobu import __version__, __logo__


class Kanobu:
    def __init__(self):
        self.lang = locale.getdefaultlocale()[0] or "en_US"
        self.version = __version__.replace("a", " \033[41m Alpha ") \
                                  .replace("b", " \033[43m\033[30m Beta ")
        self.version = f"v{self.version} "
        self.name = "Rock paper scissors"
        self.objects = ["Rock", "Scissors", "Paper"]
        self.massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]
        self.results = [
            self.black(self.green("Win")) + " ",
            self.redbg("Loss"),
            self.black(self.yellow("Draw"))
        ]

    def game(self, players):
        self.players = players

    def logo(self):
        print(self.blue(__logo__).replace("\n", "\n "))

    def battle(self, user1, user2, index=0):
        vs = self.red('vs')
        for key in self.massive[user1.choice]:
            if user2.choice == self.massive[user1.choice].index(key):
                result = self.results[key]
                index = self.gray(index)
                print(f"{index} {result} {user1.name} {vs} {user2.name}")

    def blue(self, text):
        #  \033[1;30m
        return f"\033[34m {text}\033[0m"

    def red(self, text):
        return f"\033[31m{text}\033[0m"

    def redbg(self, text):
        return f"\033[41m {text} \033[0m"

    def green(self, text):
        return f"\033[42m {text} \033[0m"

    def yellow(self, text):
        return f"\033[43m {text} \033[0m"

    def black(self, text):
        return f"\033[30m{text}\033[0m"

    def gray(self, text):
        return f"\033[1;30m{text}\033[0m"

    def test(self):
        self.battle(*self.players[::len(self.players) - 1])

        for player in self.players[0:-1]:
            ind = self.players.index(player)
            self.battle(*self.players[ind:ind + 2], ind + 1)

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {self.objects[player.choice]}")
