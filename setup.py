import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="kanobu",
    version="0.1.0",
    author="Daniel Zakharov",
    author_email="daniel734@bk.ru",
    description="Free implementation of the game \"stone, scissors, paper\"",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="kanobu game",
    url="https://github.com/jDan735/kanobu",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.4",
    install_requires=[
        "colorama",
        "cson"
    ],

    entry_points={
        "console_scripts": [
            "kanobu=kanobu.__main__:main"
        ]
    }
)
