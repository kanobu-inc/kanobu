# 🗿✂️📄 Kanobu
## 🗣 Localisation
| Language      | Status   | Language      | Status    |
|---------------|----------|---------------|-----------|
| 🇷🇺 Russian    | 👍 stable | 🇩🇪 German     | ⚠️ beta   |
| 🇺🇦 Ukrainian  | 👍 stable | 🇬🇧 English    | 👍 stable |
| 🇫🇷 French     | ⚠️ beta   | 🇪🇸 Spanish    | 🗓 plans  |
| 🇨🇳 Chinese    | ❌ none   | 🇵🇹 Portuguese | 🗓 plans  |
| 🇵🇱 Polish     | 🗓 plans  | 🇮🇹 Italian    | ⚠️ beta   |
| 🇹🇷 Turkish    | ❌ none   | 🇸🇦 Arabien    | ❌ none   |
| 🇰🇷 Korean     | ❌ none   | 🇮🇳 Hindi      | ❌ none   |
| 🇭🇺 Hungarian  | 🗓 plans  | 😀 Emoji      | ⚠️ beta   |

The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code system is used to name the localization files.
## 🧑‍💻 Installation
To install, you must download repository and dependencies:
```
git clone https://github.com/jDan735/kanobu.git
cd kanobu
pip install -r requirements.txt
```

## 🚀 Start
To start, run this code:
```
python kanobu.py
```
### ⚙️ Options
#### dev
To get developers functions (`log`, `clog`), and logs about variables and other parameters
#### lang
For set default language. All languages placed in `locale`
#### 🗓 test
Show all variables, all variants of game (`win`, `lose`, `draw`), FIXME, TODO, help information
## ⚒ Build
Build supported on all popular os (`Windows`, `Mac OS`, `Linux`). You can build for your platform, not other

Planned building for `Windows x32` and `Ubuntu x32 xenial`

To build, run this code:
```
pip install pyinstaller
pyinstaller kanobu.py --onefile
```
Then copy all files without `kanobu.py` to `dist`
## 🔨 Dependencies
### 🖌 [colorama](https://github.com/tartley/colorama)
Simple cross-platform colored terminal text in Python. Support `cmd`, `bash`
### 📄 [pycjson](https://github.com/avakar/pycson)
A Coffescript Object Notation (CSON) parser. Help write configs for humans. Based on `CoffeeScript`
## 📰 Trello (ru)
You can subscribe to [trello](https://trello.com/b/o0ozs1XT) to get information about the new functionality
