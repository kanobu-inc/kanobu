from cx_Freeze import setup, Executable

setup(
    name="kanobu",
    executables=[Executable("ropasci.py")]
)
