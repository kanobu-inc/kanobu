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

    args = parser.parse_args()

    if args.version:
        print(kanobu.version)
        return

    kanobu.logo()

    kanobu.game([Bot("#445622"),
                 Bot("Obama21"),
                 Bot("Kanobu1"),
                 Bot("jDan735")])

    kanobu.test()


if __name__ == "__main__":
    main()
