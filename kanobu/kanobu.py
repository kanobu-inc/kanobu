def main():

    import os
    import random
    import time
    import cson
    import argparse
    from colorama import init

    init()

    def red(text):
        return "\033[31m" + text + "\033[0m"

    def green(text):
        return "\033[32m" + text + "\033[0m"

    def yellow(text):
        return "\033[33m" + text + "\033[0m"

    def blue(text):
        return "\033[44m" + text + "\033[0m"

    def logo(name):
        spaces = " " * (len(name) + 2)

        print(blue(spaces))
        print(blue(" " + name + " "))
        print(blue(spaces))

    #REWRITE
    def log(text, left=False, right=True):
        if args.dev:
            leftSpace = " " if left else ""
            rightSpace = " " if right else ""

            print(leftSpace + yellow("[DEV]") + rightSpace + text)

    def clog(text, left=False, right=True):
        if args.dev:
            leftSpace = " " if left else ""
            rightSpace = " " if right else ""

            return leftSpace + yellow("[DEV]") + rightSpace + text

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dev", action="store_true", help="Dev mode")
    parser.add_argument("-t", "--test", action="store_true", help="Test mode")
    parser.add_argument("-l", "--lang", help="Your lang")

    args = parser.parse_args()
    lang = args.lang

    if lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em" and lang != "it" and lang != "fr":
        lang = input('Your language? (de, en, ru, ua, em, it, fr) ')
        while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em" and lang != "it" and lang != "fr":
            lang = input('Your language? (de, en, ru, ua, em, it, fr) ')

    log(os.path.abspath(__file__))
    path = os.path.dirname(os.path.abspath(__file__))

    log(path)

    separator = "/" if os.name == "posix" or os.name == "macos" else "\\"

    try:
        with open(path + "\\kanobu\\locale\\".replace("\\", separator) + lang + ".cson", encoding="utf-8") as locale_file:
            locale = cson.load(locale_file)
            log(locale["lang"]["name"])
    except FileNotFoundError:
        with open(path + "\\locale\\".replace("\\", separator) + lang + ".cson", encoding="utf-8") as locale_file:
            locale = cson.load(locale_file)
            log(locale["lang"]["name"])

    logo(locale["game"])

    while True:

        for key in range(3):
            print(str(key + 1) + ". " + locale["objects"][key])

        player_input = input(locale["message"]["choice"])
        while player_input != "1" and player_input != "2" and player_input != "3":
            player_input = input(locale["message"]["choice"])

        player = int(player_input) - 1
        print()

        print(locale["bot"]["choice"])
        print()

        time.sleep(1)
        bot = random.randint(0, 2)

        massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]

        i = 0
        for key in massive[player]:
            a = "" if locale["lang"]["case"] == False else locale["lang"]["case"][bot]

            object = locale["objects"][bot]
            object = object if locale["lang"]["case"] == False else object.lower()

            if bot == i:

                if i == 0:
                    print(yellow(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + a + " " + object)

                if i == 1:
                    print(green(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + a + " " + object)

                if i == 2:
                    print(red(" " + locale["results"][key] + "!") + " " + locale["bot"]["have"] + a + " " + object)

            i += 1

        print()

        play = input(locale["message"]["play"]["request"])

        if play != locale["message"]["play"]["arguments"][0]:
            break
