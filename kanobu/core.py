import locale

if __file__ == "__main__":
    from __init__ import __version__
else:
    from kanobu import __version__


class Kanobu:
    def __init__(self):
        self.lang = locale.getdefaultlocale()[0]
        self.version = __version__.replace("a", " \033[41m Alpha ") \
                                  .replace("b", " \033[43m\033[30m Beta ")
        self.version = f"v{self.version} "
        self.name = "Rock paper scissors"
        self.objects = ["Rock", "Scissors", "Paper"]
        self.kanobu_logo = [
            " _                     _           ",
            "| | ____ _ _ __   ___ | |__  _   _ ",
            "| |/ / _` | '_ \\ / _ \\| '_ \\| | | |",
            "|   < (_| | | | | (_) | |_) | |_| |",
            "|_|\\_\\__,_|_| |_|\\___/|_.__/ \\__,_|",
            "                                   "
        ]
        self.massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]
        self.results = [
            "Victory",
            "Loss",
            "Draw"
        ]

    def game(self, players):
        self.players = players

    def logo(self):
        for item in self.kanobu_logo:
            print(self.blue(item))

    def battle(self, user1, user2):
        for key in self.massive[user1.choice]:
            if user2.choice == self.massive[user1.choice].index(key):
                return self.results[key]

    def blue(self, text):
        return f"\033[34m {text}\033[0m"

    def test(self):
        return self.battle(*self.players[0:2])

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {self.objects[player.choice]}")
