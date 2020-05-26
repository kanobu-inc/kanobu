from cx_Freeze import setup, Executable

setup(
    name="kanobu",
    extras_require = {
       "build": ["cson", "colorama"]
    },
    executables=[Executable("ropasci.py")]
)
