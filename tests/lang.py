import os

owd = os.getcwd()

os.chdir(os.path.join(os.path.abspath(os.path.curdir)))

python = "python3" if os.name == "posix" or os.name == "macos" else "python"

os.system(python + " -m kanobu --lang en --choice 1")
os.system(python + " -m kanobu --lang em --choice 1")
os.system(python + " -m kanobu --lang de --choice 1")
os.system(python + " -m kanobu --lang fr --choice 1")
os.system(python + " -m kanobu --lang it --choice 1")
os.system(python + " -m kanobu --lang ru --choice 1")
os.system(python + " -m kanobu --lang ua --choice 1")

os.chdir(owd)
