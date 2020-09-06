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

    kanobu = Kanobu()

    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        action="store_true",
                        help="For version")

    kanobu.logo()

    args = parser.parse_args()

    if args.version:
        print(kanobu.version)
        return

    kanobu.game([Bot("Bot #44566"),
                 Bot("Bot #122311"),
                 Bot("Bot #fffefeefef"),
                 Bot("Bot Obama")])

    print()
    print(kanobu.test())


if __name__ == "__main__":
    main()
