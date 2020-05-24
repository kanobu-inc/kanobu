import os
import random
import time
import cson
from colorama import init

os.sys.path.insert(0, "./lib/")

from color import *

# init()

# Want colorama
# Work if dev == True
def log(text, space=False):
    if dev:
        if space:
            print(yellow(" [DEV] ") + text)
        else:
            print(yellow("[DEV] ") + text)

if len(os.sys.argv) > 1:
    dev = os.sys.argv[1] == "dev"
else:
    dev = False

lang = input('Your language? (de, en, ru, ua, em) ')

while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em":
    lang = input('Your language? (de, en, ru, ua, em) ')

with open("./locale/" + lang + ".cson", encoding="utf-8") as locale_file:
    locale = cson.load(locale_file)
    log(locale["name"])

logo(locale["game"])

while True:

    for key in range(3):
        print(str(key + 1) + ". " + locale["objects"][key])

    player = int(input(locale["message"]["choice"])) - 1
    print()

    print(locale["bot"]["choice"])
    print()

    time.sleep(1)
    bot = random.randint(0, 2)

    # ========== SHITCODES ==========
    def win():
        print(green(" " + locale["results"][0] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    def lose():
        print(red(" " + locale["results"][1] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    def draw():
        print(yellow(" " + locale["results"][2] + "!") + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    # ===============================

    log(red("red"), True)
    log(yellow("yellow"), True)
    log(green("green"), True)
    print()

    if bot == 0:
        if player == 2:
            lose()
        if player == 1:
            win()
        if player == 0:
            draw()
    if bot == 1:
        if player == 2:
            win()
        if player == 1:
            draw()
        if player == 0:
            lose()
    if bot == 2:
        if player == 2:
            draw()
        if player == 1:
            win()
        if player == 0:
            lose()

    print()

    play = input(locale["message"]["play"]["request"])

    if play != locale["message"]["play"]["arguments"][0]:
        break
