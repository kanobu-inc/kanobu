import os

owd = os.getcwd()

os.chdir(os.path.join(os.path.abspath(os.path.curdir)))

python = "python3" if os.name == "posix" or os.name == "macos" else "python"

os.system(python + " -m kanobu --lang en")
os.system(python + " -m kanobu --lang em")
os.system(python + " -m kanobu --lang de")
os.system(python + " -m kanobu --lang fr")
os.system(python + " -m kanobu --lang it")
os.system(python + " -m kanobu --lang ru")
os.system(python + " -m kanobu --lang ua")

os.chdir(owd)
