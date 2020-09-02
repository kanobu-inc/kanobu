import locale

if __file__ == "__main__":
    from __init__ import __version__
    from bot import Bot
    from user import User
else:
    from kanobu import __version__
    from kanobu.bot import Bot
    from kanobu.user import User


class Kanobu:
    def __init__(self, players):
        self.players = players
        self.lang = locale.getdefaultlocale()[0]
        self.version = f"v{__version__}"

    def rzaka(self):
        for player in self.players:
            print(f"{player.name} - {player.choice}")
