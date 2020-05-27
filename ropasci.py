import os
import random
import time
import cson
import argparse

os.sys.path.insert(0, "./lib/")
from color import *

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

if lang == "de" or lang == "en" or lang == "ru" or lang == "ua" or lang == "em":
    True
else:
    lang = input('Your language? (de, en, ru, ua, em) ')
    while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em":
        lang = input('Your language? (de, en, ru, ua, em) ')

with open("./locale/" + lang + ".cson", encoding="utf-8") as locale_file:
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

    with open("./config.cson", "r", encoding="utf-8") as config_file:
        modes = cson.load(config_file)
    massive = modes["standart"]

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
        quit()
