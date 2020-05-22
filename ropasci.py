import random
import time
import json
from colorama import init, Fore, Back, Style
from termcolor import colored

init()

lang = input('Your language? (de, en, ru) ')

while lang != "de" and lang != "en" and lang != "ru":
    lang = input('Your language? (de, en, ru) ')

with open("./locale/" + lang + ".json", encoding="utf-8") as locale_file:
    locale = json.load(locale_file)

spaces = ""
for i in range(len(locale["name"]) + 2):
    spaces += " "

print(Back.BLUE + spaces + Back.BLACK)
print(Back.BLUE + " " + locale["name"] + " " + Back.BLACK)
print(Back.BLUE + spaces + Back.BLACK)

while True:

    print('1. ' + locale["objects"][0])
    print('2. ' + locale["objects"][1])
    print('3. ' + locale["objects"][2])

    player = int(input(locale["message"]["requests"]["choice"])) - 1
    print()

    print(locale["bot"]["choice"])
    print()

    time.sleep(1)
    bot = random.randint(0, 2)

    if bot == 0:
        if player == 2:
            print(Fore.RED + " " + locale["results"][1] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 1:
            print(Fore.GREEN + " " + locale["results"][0] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 0:
            print(Fore.YELLOW + " " + locale["results"][2] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    if bot == 1:
        if player == 2:
            print(Fore.GREEN + " " + locale["results"][0] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 1:
            print(Fore.YELLOW + " " + locale["results"][2] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 0:
            print(Fore.RED + " " + locale["results"][1] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
    if bot == 2:
        if player == 2:
            print(Fore.YELLOW + " " + locale["results"][2] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 1:
            print(Fore.GREEN + " " + locale["results"][0] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])
        if player == 0:
            print(Fore.RED + " " +locale["results"][1] + "!" + Fore.WHITE + " " + locale["bot"]["have"] + " " + locale["objects"][bot])

    print()

    if input(locale["message"]["requests"]["play"]["request"]) != locale["message"]["requests"]["play"]["arguments"][0]:
        break
