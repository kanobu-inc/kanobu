import locale

if __file__ == "__main__":
    from __init__ import __version__
else:
    from kanobu import __version__


class Kanobu:
    def __init__(self):
        self.lang = locale.getdefaultlocale()[0] or "en_US"
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
            self.black(self.green("Win")) + " ",
            self.redbg("Loss"),
            self.black(self.yellow("Draw"))
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
        print(f"{self.gray('0.')} {self.battle(self.players[0], self.players[-1])} {self.players[0].name} {self.red('vs')} {self.players[3].name}")
        print(f"{self.gray('1.')} {self.battle(*self.players[0:2])} {self.players[0].name} {self.red('vs')} {self.players[1].name}")
        print(f"{self.gray('2.')} {self.battle(*self.players[1:3])} {self.players[1].name} {self.red('vs')} {self.players[2].name}")
        return f"{self.gray('3.')} {self.battle(*self.players[2:4])} {self.players[2].name} {self.red('vs')} {self.players[3].name}"

        # print(f"\033[1;30m0.\033[0m {self.result} {self.players[0].name}")
        # return f"\033[1;30m1.\033[0m {self.result} {self.players[1].name}"

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {self.objects[player.choice]}")
