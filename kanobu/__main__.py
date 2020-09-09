import argparse
from colorama import init
try:
    from kanobu.core import Kanobu

except ModuleNotFoundError:
    from core import Kanobu

if __file__ == "__main__":
    from bot import Bot
    from user import User
else:
    from kanobu.bot import Bot
    from kanobu.user import User


def main():
    init()

    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        action="store_true",
                        help="For version")

    parser.add_argument("-s",
                        "--sqlite",
                        action="store_true",
                        help="For save to sqlite db")

    parser.add_argument("-l",
                        "--lang",
                        help="lang")

    args = parser.parse_args()

    if args.lang:
        kanobu = Kanobu(args.lang)
    else:
        kanobu = Kanobu()

    if args.version:
        print(kanobu.version)
        return

    kanobu.game([Bot("#4323245622"),
                 Bot("Obama"),
                 Bot("Kanobu"),
                 Bot("jDan735")])

    if args.sqlite:
        kanobu.writeResultToSQLite()

    kanobu.showResults()


if __name__ == "__main__":
    main()
