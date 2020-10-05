import locale
import yaml
import os
import sqlite3
from prettytable import PrettyTable

try:
    from kanobu.color import green, black, blue, red, yellow

except ModuleNotFoundError:
    from color import green, black, blue, red, yellow

if __file__ == "__main__":
    from __init__ import __version__, __logo__
else:
    from kanobu import __version__, __logo__


class Event:
    def __init__(self, name, localename):
        self.colors = {
            "win": "\033[30m\033[32m",
            "loss": "\033[31m",
            "draw": "\033[30m\033[33m"
        }
        self.end = "\033[0m"
        self.tname = localename
        self.name = f"{self.colors[name]}{localename}{self.end}"


class Kanobu:
    def __init__(self, lang=False):
        self.lang = lang if lang else locale.getdefaultlocale()[0] or "en_US"
        self.version = __version__.replace("a", " \033[41m Alpha ") \
                                  .replace("b", " \033[43m\033[30m Beta ") + " \033[0m"
        self.version = f"v{self.version} "
        self.locale = self.getLocale(self.lang)
        self.name = "Rock paper scissors"
        self.objects = ["Rock", "Scissors", "Paper"]
        self.massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]
        self.results = [
            Event("win", self.locale["results"][0]),
            Event("loss", self.locale["results"][1]),
            Event("draw", self.locale["results"][2])
        ]
        self.td = []
        self.th = ['#', 'Result', 'Player1', 'Player2']

    def getLocale(self, lang):
        path = os.path.dirname(os.path.abspath(__file__))
        s = "\\" if os.name == "nt" else "/"
        with open(f"{path}{s}locale{s}{lang}.yaml",
                  encoding="utf-8") as locale_file:
            return yaml.safe_load(locale_file.read())

    def logo(self, len1=0):
        if len1 == 0:
            len1 = len(str(PrettyTable(self.locale["headers"])).split("\n")[0])
        len2 = len(__logo__.split("\n")[2])

        num = len1 - len2
        padding = int(num / 2) * ' '
        print(padding[:-1] + blue(__logo__).replace("\n", f"\n{padding}"))

    def battle(self, user1, user2, index=0):
        for key in self.massive[user1.choice]:
            if user2.choice == self.massive[user1.choice].index(key):
                result = self.results[key]
                return [index, result, user1, user2]

    def game(self, players, ind_num=0):
        self.players = players

        if len(self.players) <= 1:
            print(red("Для игры необходимо хотя бы 2 игрока"))
            return

        if len(self.players) > 3:
            a = self.battle(*self.players[::len(self.players) - 1])
            self.td.extend(a)
            ind_num = 1

        for player in self.players[0:-1]:
            ind = self.players.index(player)
            a = self.battle(*self.players[ind:ind + 2], ind + ind_num)
            self.td.extend(a)

    def writeResultToSQLite(self):
        self.td_copy = self.td.copy()
        for index, item in enumerate(self.td_copy):
            if type(item).__name__ == "Event":
                self.td_copy[index] = item.tname

            if type(item).__name__ == "Bot":
                self.td_copy[index] = item.tname

            if type(item).__name__ == "User":
                self.td_copy[index] = item.name

        conn = sqlite3.connect("result.db")
        cursor = conn.cursor()

        a = '\"' + '\" text, \"'.join(self.locale['headers']) + '\" text'
        cursor.execute(f"CREATE TABLE albums ({a})")

        columns = len(self.locale["headers"])

        td_data = self.td_copy[:]
        changes = []

        while td_data:
            column = tuple(td_data[:columns])

            changes.append(column)

            td_data = td_data[columns:]

        cursor.executemany("INSERT INTO albums VALUES (?,?,?,?)", changes)

        conn.commit()

    def showResults(self):
        columns = len(self.locale["headers"])

        table = PrettyTable(self.locale["headers"])

        table.align = "l"

        for index, item in enumerate(self.td):
            if type(item).__name__ == "Event":
                self.td[index] = item.name

            if (type(item).__name__ == "Bot" or
                type(item).__name__ == "Event" or
                type(item).__name__ == "User"):
                self.td[index] = item.name

        td_data = self.td[:]

        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]

        self.logo(len(str(table).split("\n")[0]))

        print(table)
