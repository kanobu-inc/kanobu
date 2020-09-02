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

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {player.choice}")
