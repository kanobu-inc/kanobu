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
