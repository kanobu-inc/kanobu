from cx_Freeze import setup, Executable

setup(
    name = "kanobu",
    version = "1.0",
    description = "kanobu",
    executables = [Executable("ropasci.py")]
)
