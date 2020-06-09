def main():

    import os
    import random
    import time
    import yaml
    import argparse
    import locale
    from kanobu.color import red, green, yellow, blue, logo
    from kanobu import __version__

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
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-c", "--choice", help="Enter choice without input")
    parser.add_argument("-l", "--lang", help="Your lang")

    args = parser.parse_args()

    path = os.path.dirname(os.path.abspath(__file__))

    if args.version:
        print(__version__)
        quit()

    if args.lang == None:
        lang = locale.getdefaultlocale()[0]

    elif (args.lang == "de_DE" or
          args.lang == "en_EN" or
          args.lang == "ru_RU" or
          args.lang == "ua_UA" or
          args.lang == "em_EM" or
          args.lang == "it_IT" or
          args.lang == "fr_FR"):

         lang = args.lang

    else:
        print(red("[ERROR]") + " Not supported locale")
        print(yellow("[NOTE]") + " Write locale as ru_RU")
        quit()




    # if lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em" and lang != "it" and lang != "fr":
    #     lang = input('Your language? (de, en, ru, ua, em, it, fr) ')
    #     while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em" and lang != "it" and lang != "fr":
    #         lang = input('Your language? (de, en, ru, ua, em, it, fr) ')

    log(os.path.abspath(__file__))

    log(path)

    separator = "/" if os.name == "posix" or os.name == "macos" else "\\"

    try:
        with open(path + "\\kanobu\\locale\\".replace("\\", separator) + lang + ".yaml", encoding="utf-8") as locale_file:
            locale = yaml.safe_load(locale_file)
            log(locale["lang"]["name"])
    except FileNotFoundError:
        with open(path + "\\locale\\".replace("\\", separator) + lang + ".yaml", encoding="utf-8") as locale_file:
            locale = yaml.safe_load(locale_file)
            log(locale["lang"]["name"])

    while True:
        logo(locale["game"])
        for key in range(3):
            print(str(key + 1) + ". " + locale["objects"][key])

        log("args.choice: " + str(args.choice))
        log("args.choice == False: " + str(args.choice == False))

        if args.choice == None:
            player_input = input(locale["message"]["choice"])
        else:
            if args.choice == "1" or args.choice == "2" or args.choice == "3":
                player_input = args.choice
                print(locale["message"]["choice"] + args.choice)
            else:
                print(red("[ERROR]") + " Use 1, 2, 3 for choice")
                quit()

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
                    color_message = yellow(" " + locale["results"][key] + "!")

                if i == 1:
                    color_message = green(" " + locale["results"][key] + "!")

                if i == 2:
                    color_message = red(" " + locale["results"][key] + "!")

                print(color_message + " " + locale["bot"]["have"] + a + " " + object)

            i += 1

        print()

        play = input(locale["message"]["play"]["request"])

        if play != locale["message"]["play"]["arguments"][0]:
            break
