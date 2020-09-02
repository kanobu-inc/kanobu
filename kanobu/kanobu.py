def main():

    import os
    import random
    import time
    import yaml
    import argparse
    import locale
    from kanobu.color import red, green, yellow, logo
    from kanobu import __version__

    def log(text, left=False, right=True):
        if args.dev:
            leftSpace = " " if left else ""
            rightSpace = " " if right else ""

            print(f"{leftSpace}{yellow('[DEV]')}{rightSpace}{text}")

    def clog(text, left=False, right=True):
        if args.dev:
            leftSpace = " " if left else ""
            rightSpace = " " if right else ""

            return f"{leftSpace}{yellow('[DEV]')}{rightSpace}{text}"

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dev", action="store_true", help="Dev mode")
    parser.add_argument("-t", "--test", action="store_true", help="Test mode")
    parser.add_argument("-v", "--version", action="store_true", help="For version")
    parser.add_argument("-c", "--choice", help="Enter choice without input")
    parser.add_argument("-l", "--lang", help="Your lang")

    args = parser.parse_args()

    log(locale.getdefaultlocale()[0])

    path = os.path.dirname(os.path.abspath(__file__))
    separator = "/" if os.name == "posix" or os.name == "macos" else "\\"

    if args.version:
        print(f"v{__version__}")
        quit()

    langfile = locale.getdefaultlocale()[0] if args.lang == None else args.lang

    try:
        open(path + "/locale/".replace("/", separator) + langfile + ".yaml")
    except FileNotFoundError:
        for file in os.listdir(path + "/locale/".replace("/", separator)):
            # file = file.replace(".yaml", "")
            log(file)
            if file[0] + file[1] == langfile[0] + langfile[1]:
                with open(f"{path}{'/locale/'.replace('/', separator)}{file}") as localefile1:
                    if yaml.safe_load(localefile1.read())["lang"]["default"]:
                        langfile = file.replace(".yaml", "")
    try:
        with open(f"{path}{'/kanobu/locale/'.replace('/', separator)}{langfile}.yaml", encoding="utf-8") as locale_file:
            locale = yaml.safe_load(locale_file)
            log(locale["lang"]["name"])
    except FileNotFoundError:
        with open(f"{path}{'/locale/'.replace('/', separator)}{langfile}.yaml", encoding="utf-8") as locale_file:
            locale = yaml.safe_load(locale_file)
            log(locale["lang"]["name"])

    while True:
        logo(locale["game"])
        for key in range(3):
            print(f"{str(key + 1)}. {locale['objects'][key]}")

        log(f"args.choice: {str(args.choice)}")
        log(f"args.choice == False: {str(args.choice is False)}")

        if args.choice is None:
            player_input = input(locale["message"]["choice"])
        else:
            if args.choice == "1" or \
               args.choice == "2" or \
               args.choice == "3":
                player_input = args.choice
                print(f"{locale['message']['choice']}{args.choice}")
            else:
                print(f"{red('[ERROR]')} Use 1, 2, 3 for choice")
                quit()

        while (player_input != "1" and
               player_input != "2" and
               player_input != "3"):
            player_input = input(locale["message"]["choice"])

        player = int(player_input) - 1
        print()

        print(f"{locale['bot']['choice']}.", end="")
        time.sleep(0.6)

        print(".", end="")
        time.sleep(0.2)

        print(".")
        time.sleep(0.3)

        print()
        time.sleep(0.2)

        bot = random.randint(0, 2)

        massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]

        i = 0
        for key in massive[player]:
            a = "" if locale["lang"]["case"] is False else locale["lang"]["case"][bot]

            object = locale["objects"][bot]
            object = object if locale["lang"]["case"] is False else object.lower()

            if bot == i:

                if i == 0:
                    message = yellow(f" {locale['results'][key]}!")

                if i == 1:
                    message = green(f" {locale['results'][key]}!")

                if i == 2:
                    message = red(f" {locale['results'][key]}!")

                print(f"{message} {locale['bot']['have']}{a} {object}")

            i += 1

        print()

        play = input(locale["message"]["play"]["request"])

        if play != locale["message"]["play"]["arguments"][0]:
            break
