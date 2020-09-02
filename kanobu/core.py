import locale

if __file__ == "__main__":
    from __init__ import __version__
else:
    from kanobu import __version__


class Kanobu:
    def __init__(self, players):
        self.players = players
        self.lang = locale.getdefaultlocale()[0]
        self.version = f"v{__version__}"
        self.name = "Rock paper scissors"
        self.objects = ["Rock", "Scissors", "Paper"]

    def logo(self):
        self.spaces = " " * (len(self.name) + 2)

        print(self.blue(self.spaces))
        print(self.blue(f" {self.name} "))
        print(self.blue(self.spaces))

    def blue(self, text):
        return "\033[44m" + text + "\033[0m"

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {self.objects[player.choice]}")
