import random
import time
import json
import os
from colorama import init, Fore, Back

init()

# Want colorama
# Want os
# Work if dev == True
def log(text, space=False):
    if dev:
        if space:
            print(Fore.YELLOW + " [DEV] " + Fore.WHITE + text)
        else:
            print(Fore.YELLOW + "[DEV] " + Fore.WHITE + text)

if len(os.sys.argv) > 1:
    dev = os.sys.argv[1] == "dev"
else:
    dev = False

lang = input('Your language? (de, en, ru, ua, em) ')

while lang != "de" and lang != "en" and lang != "ru" and lang != "ua" and lang != "em":
    lang = input('Your language? (de, en, ru, ua, em) ')

with open("./locale/" + lang + ".json", encoding="utf-8") as locale_file:
    locale = json.load(locale_file)
    log(locale["name"])

spaces = " " * (len(locale["game"]) + 2)

print(Back.BLUE + spaces + Back.BLACK)
print(Back.BLUE + " " + locale["game"] + " " + Back.BLACK)
print(Back.BLUE + spaces + Back.BLACK)

while True:

    for key in range(3):
        print(str(key + 1) + ". " + locale["objects"][key])

    player = int(input(locale["message"]["requests"]["choice"])) - 1
    print()

    print(locale["bot"]["choice"])
    print()

    time.sleep(1)
    bot = random.randint(0, 2)

    # ========== SHITCODES ==========
    def win():
        print(Fore.GREEN + " " + locale["results"][0] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    def lose():
        print(Fore.RED + " " + locale["results"][1] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    def draw():
        print(Fore.YELLOW + " " + locale["results"][2] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    # ===============================

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

    play = input(locale["message"]["requests"]["play"]["request"])

    if play != locale["message"]["requests"]["play"]["arguments"][0]:
        break
