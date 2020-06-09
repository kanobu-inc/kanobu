import os

owd = os.getcwd()

os.chdir(os.path.join(os.path.abspath(os.path.curdir)))

python = "python3" if os.name == "posix" or os.name == "macos" else "python"

os.system(python + " -m kanobu --lang en_EN --choice 1")
os.system(python + " -m kanobu --lang em_EM --choice 1")
os.system(python + " -m kanobu --lang de_DE --choice 1")
os.system(python + " -m kanobu --lang fr_FR --choice 1")
os.system(python + " -m kanobu --lang it_IT --choice 1")
os.system(python + " -m kanobu --lang ru_RU --choice 1")
os.system(python + " -m kanobu --lang ua_UA --choice 1")

os.chdir(owd)
