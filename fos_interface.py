# greeting shell

from this import c, d, i, s
print()
help()
from sys import platform
from subprocess import run
from os import system
system("cmd")
system("powershell")
system("wmic")
print(f'Python 3.8.5 (default, Jul 20 2020, 23:11:29) [GCC 9.3.0] on {platform}\nType "help", "copyright", "credits", or "license" for more information.\nType "fos" or "" to boot up Froggy OS.\nType "readme" to see guide fos Froggy OS.')
while True:
    xxxxxyyyyyzzzzz = input(">>> ")
    if xxxxxyyyyyzzzzz == "" or xxxxxyyyyyzzzzz == "fos":
        break
    elif xxxxxyyyyyzzzzz == "readme":
        f = open("readme.txt", "r")
        print(f.read())
        f.close()
    else:
        try:
            run(xxxxxyyyyyzzzzz.split(" "))
        except Exception:
            try:
                print(eval(xxxxxyyyyyzzzzz))
            except Exception:
                try:
                    exec(xxxxxyyyyyzzzzz)
                except Exception as e:
                    system(xxxxxyyyyyzzzzz)
print("Current Version: FOS 1.71.0 -- The Update of Great Farewell")
print("Froggy OS, TUI made by Can Koyuncu, nickname: @Lava-Salt, visit \"https://github.com/Lava-salt/fos.git/\"")
print("To contact me, go to \"https://github.com/Lava-salt/fos/discussions/\"")
print("Check out my other works: \"https://github.com/Lava-salt/side_projects.git\"")
print("GitHub User List of Fame in Making of FOS:")
print("@Lava-salt (Administrator)")

# head (module importing)

from fos_sourcecode import *
from datetime import datetime, MAXYEAR, MINYEAR, UTC
import calendar # calendar module is actually used for printing calendar through an "exec" function
from time import sleep, altzone, daylight, timezone, tzname
from webbrowser import open as web
from webbrowser import open_new_tab
from random import randint, random, gauss, normalvariate, shuffle, choice
from os import getcwd, chdir, mkdir, listdir, remove, rename, EX_OK, F_OK, O_APPEND, O_BINARY, O_CREAT, O_EXCL, O_NOINHERIT, O_RANDOM, O_RDONLY, O_RDWR, O_SEQUENTIAL, O_SHORT_LIVED, O_TEMPORARY, O_TEXT, O_TRUNC, O_WRONLY, P_DETACH, P_NOWAIT, P_NOWAITO, P_OVERLAY, P_WAIT, R_OK, SEEK_CUR, SEEK_END, SEEK_SET, TMP_MAX, W_OK, X_OK, altsep, curdir, defpath, devnull, environ, extsep, linesep, name, pardir, pathsep, sep, supports_bytes_environ
from os import path as pathos
from sys import __stderr__, __stdin__, __stdout__, api_version, argv, base_exec_prefix, base_prefix, builtin_module_names, byteorder, copyright, dllhandle, dont_write_bytecode, exec_prefix, executable, flags, float_info, float_repr_style, hash_info, hexversion, implementation, int_info, maxsize, maxunicode, meta_path, modules, orig_argv, path, path_hooks, path_importer_cache, platlibdir, prefix, pycache_prefix, stderr, stdin, stdlib_module_names, stdout, thread_info, version, version_info, warnoptions, winver
from subprocess import CalledProcessError, call, Popen, ABOVE_NORMAL_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, CREATE_BREAKAWAY_FROM_JOB, CREATE_DEFAULT_ERROR_MODE, CREATE_NEW_CONSOLE, CREATE_NEW_PROCESS_GROUP, CREATE_NO_WINDOW, DETACHED_PROCESS, DEVNULL, HIGH_PRIORITY_CLASS, IDLE_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, PIPE, REALTIME_PRIORITY_CLASS
from subprocess import PIPE as SPPIPE
from codecs import encode
from math import e, inf, nan, pi, tau
print("Before entering, please manage modules.")
try:
    import nltk
    nltk.download('words')
    from nltk.corpus import words
    import enchant
except Exception as e: pass
while True:
    print("1 to install modules")
    print("2 to uninstall modules")
    print("3 to reinstall modules")
    print("4 to finish")
    x = input("\n")
    if x == "himil":
        print("Welcome to Himil!")
        print("Now, a Python shell will open.")
        print("It closes after 5 executions.")
        print("You can extend the closing time by 5 with \"extend\".")
        print("Ready, Mrs. Cow Pepper?")
        tmmlptealpaitafnfal = 5
        while not(tmmlptealpaitafnfal <= 0):
            tmmlptealpaitafnfal2 = input(f"Remaining: {tmmlptealpaitafnfal}\n>>> ")
            if tmmlptealpaitafnfal2 == "extend":
                tmmlptealpaitafnfal += 5
            else:
                exec(tmmlptealpaitafnfal2)
            tmmlptealpaitafnfal -= 1
        print("Now, Flea Rat, a Batch shell with same logic will open.\nGood l(i)ck!")
        tmmlptealpaitafnfal = 5
        while not (tmmlptealpaitafnfal <= 0):
            tmmlptealpaitafnfal2 = input(f"Remaining: {tmmlptealpaitafnfal}\n>>> ")
            if tmmlptealpaitafnfal2 == "extend":
                tmmlptealpaitafnfal += 5
            else:
                system(tmmlptealpaitafnfal2)
            tmmlptealpaitafnfal -= 1
        print("Himil turned to Himilis.")
        print("Mom's Whale Hand compiled successfully.")
    else:
        x = int(x)
        if x == 1:
            system("pip install nltk")
            system("pip install pyenchant")
            system("pip install matplotlib")
            system("pip install urwid")
        elif x == 2:
            system("pip uninstall nltk")
            system("pip uninstall pyenchant")
            system("pip uninstall matplotlib")
            system("pip uninstall urwid")
        elif x == 3:
            system("pip uninstall nltk")
            system("pip uninstall pyenchant")
            system("pip uninstall matplotlib")
            system("pip uninstall urwid")
            for i in range(2):
                system("pip install nltk")
                system("pip install pyenchant")
                system("pip install matplotlib")
                system("pip install urwid")
        elif x == 4:
            print("Now some files will be compulsorily installed.")
            print("Please wait until said elseway.")
            break
import nltk
nltk.download('words')
from nltk.corpus import words
import enchant
from matplotlib import __bibtex__, color_sequences, colormaps, defaultParams, multivar_colormaps, rcParams, rcParamsDefault, rcParamsOrig
from urwid import ACTIVATE, ANY, BLACK, BOTTOM, BOX, BROWN, CENTER, CLIP, CURSOR_DOWN, CURSOR_LEFT, CURSOR_MAX_LEFT, CURSOR_MAX_RIGHT, CURSOR_PAGE_DOWN, CURSOR_PAGE_UP, CURSOR_RIGHT, CURSOR_UP, DARK_BLUE, DARK_CYAN, DARK_GRAY, DARK_GREEN, DARK_MAGENTA, DARK_RED, DEFAULT, ELLIPSIS, FIXED, FLOW, GIVEN, LEFT, LIGHT_BLUE, LIGHT_CYAN, LIGHT_GRAY, LIGHT_GREEN, LIGHT_MAGENTA, LIGHT_RED, MIDDLE, PACK, REDRAW_SCREEN, RELATIVE, RELATIVE_100, RIGHT, SPACE, TOP, UPDATE_PALETTE_ENTRY, VERSION, WEIGHT, WHITE, YELLOW, __annotations__, __version_tuple__, command_map, default_layout, detected_encoding
print("Module importing process finished.")
input("Now, booting up...\n")

# head (other functions' defining)

notebook = []
for i in range(200000):
    notebook.append("Empty")
todo = []
for i in range(200000):
    notebook.append("Empty")
todo_done = []
for i in range(200000):
    notebook.append("Not Done")
todo_fav = []
for i in range(200000):
    notebook.append("Not Favourite")
cl = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
fruits = []
for i in range(200000):
    fruits.append("This slot is empty.")
stripguide = {1: "strip", 2: "lstrip", 3: "rstrip"}
xox = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"]
rps = ["r", "p", "s"]
hanoi0 = []
hanoi1 = [1, 2, 3, 4, 5]
hanoi2 = []
hanoi3 = []
firsttime = True
bmn = ["Bing", "Google", "Yandex", "DuckDuckGo", "Yahoo!"]
bm = ["https://www.bing.com/", "https://www.google.com/", "https://ya.ru/", "https://duckduckgo.com/",
      "https://www.yahoo.com/"]
url = ["http://www.pizza.net/", "http://www.links.net/re/intro.html", "http://www.yahoo.com/",
                        "http://whitehouse.gov/", "http://geocities.com/Hollywood/Bungalow/4720/",
                        "http://www.fogcam.org/", "http://www.ebay.com/aw/welcome.html", "http://www.spacejam.com/",
                        "http://www.mcdonalds.com/a_food/", "http://www.apple.com/", "http://www.ty.com/",
                        "http://www.heavensgate.com/", "http://www.pepsi.com/", "http://www.year2000.com/",
                        "http://www.askjeeves.com/", "http://www.geocities.com/Heartland/Bluffs/4157/hampdance.html",
                        "http://www.google.com/", "http://www.netflix.com/", "http://zombo.com/",
                        "http://www.wikipedia.org/wiki/Wikipedia", "http://friendster.com/info/moreinfo.jsp",
                        "http://www.myspace.com/", "http://www.thefacebook.com/",
                        "http://www.milliondollarhomepage.com/", "http://www.reddit.com/", "https://www.mcdonalds.com/",
                        "https://www.nike.com/", "https://www.apple.com/", "https://www.starbucks.com/",
                        "https://www.amazon.com/", "https://www.pepsi.com/", "https://twitter.com/",
                        "https://www.snapchat.com/", "https://www.nasa.gov/", "https://www.google.com/",
                        "https://www.android.com/", "https://open.spotify.com/"]
kai = ["🟦", "🟩", "🟨", "🟧", "🟫", "⬜", "🟪", "🟥"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", " ", " ", " ", " ", " ", " ", " ", " "]
gods_abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "<", ">", "+", "-", "[", "]", " "]
ohno = words.words()
# it is called "ohno" because it's so long
# and like "oh no! the FOS will crash because the list is so long!"
binary = 0
names = ['Alexander', 'Alexei', 'Anatolyevich', 'Andrei', 'Andreyevich', 'Boris', 'Borisovich', 'Dmitriy', 'Dmitry', 'Fyodorovich', 'Georgy', 'Grigoriy', 'Igor', 'Ilyich', 'Joseph', 'Konstantin', 'Lavrentiy', 'Leonid', 'Lev', 'Maximilianovich', 'Mikhail', 'Mikhaylovich', 'Nikita', 'Nikolai', 'Nikolayevich', 'Pavlovich', 'Sergeyevich', 'Stepanovich', 'Ustinovich', 'Viassarionovich', 'Viktor', 'Viktorovich', 'Vladimir', 'Vladimirovich', 'Vyacheslav', 'Yevseyevich', 'Yuri']
shuffle(names)
food = "🍎🍐🍊🍌🍋"
weather = ["☀ Sunny", "☁️ Cloudy", "🌧️ Rainy", "❄️ Snowy", "⚡ Thunderstorm"]
selectedw = choice(weather)
temp = int(gauss(14, 14))
xoxguide = {"A" : "⬜", "X" : "❌", "O" : "⭕"}
ns = ["N", "S"]
we = ["W", "E"]
marks = [".", "?", "!", "!?"]
dots = ["", "", "", ",", ";", ":"]
people = ["A child", "A son", "A daughter", "A boy", "A girl", "A teen", "An adult", "A man", "A father", "A woman", "A mother", "An elder", "A grandfather", "A grandmother", "A comrade"]
sins = ["is being too sexual", "is over-eating", "is arrogant", "is lazy", "is too angry", "is greedy", "is jealous", "is defending Capitalism", "is defending Fascism", "is a Bourgeois", "is critisizing the government", "is stealing", "is critisizing"]
tf = [True, False]
drd = ["Nun", "Gimel", "He", "Shin"]
docs = ['!=', '"', '"""', '%', '%=', '&', '&=', "'", "'''", '(', ')', '*', '**', '**=', '*=', '+', '+=', ',', '-', '-=', '.', '...', '/', '//', '//=', '/=', ':', ':=', '<', '<<', '<<=', '<=', '<>', '==', '>', '>=', '>>', '>>=', '@', 'False', 'J', 'None', 'PIL', 'True', '[', '\\', ']', '^', '^=', '_', '__', '__builtins__', '__cached__', '__doc__', '__file__', '__hello__', '__loader__', '__name__', '__package__', '__phello__', '__spec__', '_abc', '_aix_support', '_android_support', '_ast', '_asyncio', '_bisect', '_blake2', '_bz2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_collections_abc', '_colorize', '_compat_pickle', '_compression', '_contextvars', '_csv', '_ctypes', '_ctypes_test', '_datetime', '_decimal', '_elementtree', '_functools', '_hashlib', '_heapq', '_imp', '_interpchannels', '_interpqueues', '_interpreters', '_io', '_ios_support', '_json', '_locale', '_lsprof', '_lzma', '_markupbase', '_md5', '_multibytecodec', '_multiprocessing', '_opcode', '_opcode_metadata', '_operator', '_osx_support', '_overlapped', '_pickle', '_py_abc', '_pydatetime', '_pydecimal', '_pyio', '_pylong', '_pyrepl', '_queue', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_sitebuiltins', '_socket', '_sqlite3', '_sre', '_ssl', '_stat', '_statistics', '_string', '_strptime', '_struct', '_symtable', '_sysconfig', '_testbuffer', '_testcapi', '_testclinic', '_testclinic_limited', '_testconsole', '_testimportmultiple', '_testinternalcapi', '_testlimitedcapi', '_testmultiphase', '_testsinglephase', '_thread', '_threading_local', '_tkinter', '_tokenize', '_tracemalloc', '_typing', '_uuid', '_virtualenv', '_warnings', '_weakref', '_weakrefset', '_winapi', '_wmi', '_zoneinfo', '`', 'abc', 'and', 'antigravity', 'argparse', 'array', 'as', 'assert', 'ast', 'async', 'asyncio', 'atexit', 'await', 'b"', "b'", 'backend_interagg', 'base64', 'bdb', 'binascii', 'bisect', 'blessings', 'break', 'builtins', 'bz2', 'cProfile', 'calendar', 'certifi', 'charset_normalizer', 'class', 'click', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorama', 'colorsys', 'compileall', 'concurrent', 'configparser', 'contextlib', 'contextvars', 'continue', 'contourpy', 'copy', 'copyreg', 'csv', 'ctypes', 'curses', 'cycler', 'dataclasses', 'datalore', 'datetime', 'dateutil', 'dbm', 'decimal', 'def', 'del', 'difflib', 'dis', 'doctest', 'elif', 'else', 'email', 'enchant', 'encodings', 'ensurepip', 'enum', 'errno', 'except', 'exit', 'f"', "f'", 'faulthandler', 'filecmp', 'fileinput', 'finally', 'fnmatch', 'fontTools', 'for', 'fos_interface', 'fos_sourcecode', 'fractions', 'from', 'ftplib', 'functools', 'gc', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'global', 'graphlib', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'idlelib', 'idna', 'if', 'imaplib', 'import', 'importlib', 'in', 'inspect', 'io', 'ipaddress', 'is', 'itertools', 'j', 'joblib', 'json', 'keyword', 'keywords', 'kiwisolver', 'lambda', 'linecache', 'linkify_it', 'locale', 'logging', 'lzma', 'mailbox', 'markdown_it', 'marshal', 'math', 'matplotlib', 'mdit_py_plugins', 'mdurl', 'mimetypes', 'mmap', 'modulefinder', 'modules', 'msvcrt', 'multiprocessing', 'netrc', 'nltk', 'nonlocal', 'not', 'nt', 'ntpath', 'nturl2path', 'numbers', 'numpy', 'opcode', 'operator', 'optparse', 'or', 'os', 'packaging', 'pass', 'pathlib', 'pdb', 'perlin_noise', 'pickle', 'pickletools', 'pip', 'pkgutil', 'platform', 'platformdirs', 'plistlib', 'poplib', 'posixpath', 'pprint', 'profile', 'prompt_toolkit', 'pstats', 'pty', 'py_compile', 'pyclbr', 'pydoc', 'pydoc_data', 'pyexpat', 'pygments', 'pylab', 'pyparsing', 'q', 'queue', 'quit', 'quopri', 'r"', "r'", 'raise', 'random', 're', 'regex', 'reprlib', 'return', 'rich', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'sitecustomize', 'six', 'smtplib', 'socket', 'socketserver', 'sqlite3', 'sre_compile', 'sre_constants', 'sre_parse', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'symbols', 'symtable', 'sys', 'sysconfig', 'tabnanny', 'tarfile', 'tempfile', 'test', 'textual', 'textwrap', 'this', 'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'tomllib', 'topics', 'tqdm', 'trace', 'traceback', 'tracemalloc', 'try', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'typing_extensions', 'u"', "u'", 'uc_micro', 'unicodedata', 'unittest', 'urllib', 'urllib3', 'urwid', 'uuid', 'venv', 'warnings', 'wave', 'wcwidth', 'weakref', 'webbrowser', 'while', 'winreg', 'winsound', 'with', 'wsgiref', 'xml', 'xmlrpc', 'xxsubtype', 'yield', 'zipapp', 'zipfile', 'zipimport', 'zlib', 'zoneinfo', '|', '|=', '~']
batch = ['assoc', 'attrib', 'break', 'bcdedit', 'cacls', 'call', 'cd', 'chcp', 'chdir', 'chkdsk', 'chkntfs', 'cls', 'cmd', 'color', 'comp', 'compact', 'convert', 'copy', 'date', 'del', 'dir', 'diskpart', 'doskey', 'driverquery', 'echo', 'endlocal', 'erase', 'exit', 'fc', 'find', 'findstr', 'for', 'format', 'fsutil', 'ftype', 'goto', 'gpresult', 'help', 'icacls', 'if', 'label', 'md', 'mkdir', 'mklink', 'mode', 'more', 'move', 'openfiles', 'path', 'pause', 'popd', 'print', 'prompt', 'pushd', 'rd', 'recover', 'rem', 'ren', 'rename', 'replace', 'rmdir', 'robocopy', 'set', 'setlocal', 'sc', 'schtasks', 'shift', 'shutdown', 'sort', 'start', 'subst', 'systeminfo', 'tasklist', 'taskkill', 'time', 'title', 'tree', 'type', 'ver', 'verify', 'vol', 'xcopy', 'wmic', '']
echo = ['cd', 'chdir', 'dir', 'driverquery', 'gpresult', 'openfiles', 'set', 'systeminfo', 'tasklist', 'type', 'help']

# body (code)

while True:
    list = [] # trust me this is necessary
    print("1 to open APPS")
    print("2 to open ASCII editor")
    print("3 to open code/OS archives")
    print("4 to edit text")
    print("5 to access internet")
    x = int(input("\n"))
    if x == 1:
        print("1 to open apps in LOCAL WIRELESS")
        print("2 to open apps in online")
        x = int(input("\n"))
        if x == 1:
            print("1 to open calculator")
            print("2 open notebook")
            print("3 to open to-do")
            print("4 to open clock")
            print("5 to open games")
            print("6 to open chat")
            print("7 to open FOS Sub-Operating System")
            print("8 to open CODE SCRAPS")
            x = int(input("\n"))
            if x == 1:
                print("1 to do addition")
                print("2 to do subtraction")
                print("3 to do multiplication")
                print("4 to do division")
                print("5 to do modulo")
                print("6 to do exponentiation")
                print("7 to do integer division")
                print("8 to do root")
                x = int(input("\n"))
                if x == 1:
                    operation("+")
                elif x == 2:
                    operation("-")
                elif x == 3:
                    operation("*")
                elif x == 4:
                    operation("/")
                elif x == 5:
                    operation("%")
                elif x == 6:
                    operation("**")
                elif x == 7:
                    operation("//")
                elif x == 8:
                    sqrt()
            elif x == 2:
                print("200,000-slot memory notebook")
                print("1 to add new note")
                print("2 to delete note")
                print("3 to see note")
                print("4 to restart notebook")
                print("5 to view notebook")
                x = int(input("\n"))
                if x == 1:
                    x = int(input("What slot would you like to enter your note? "))
                    y = input("What's your note? ")
                    notebook[x] = y
                elif x == 2:
                    x = int(input("What slot would you like to delete? "))
                    notebook[x] = "Empty"
                elif x == 3:
                    x = int(input("What slot would you like to see? "))
                    print(notebook[x])
                elif x == 4:
                    x = input(
                        "Would you really like to clear the entire notebook?\nAll the data will be lost forever.\nAre you sure? (y/n)\n")
                    if "y" in x.lower():
                        del notebook
                        notebook = []
                        for i in range(200000):
                            notebook.append("Empty")
                        print("Notebook cleared")
                elif x == 5:
                    for x in range(200000):
                        if not (notebook[x] == "Empty"):
                            print(f"{x}. {notebook[x]}")
            elif x == 3:
                print("200,000-slot memory to-do list")
                print("1 to add new task")
                print("2 to delete task")
                print("3 to see task")
                print("4 to restart to-do list")
                print("5 to view entire list")
                x = int(input("\n"))
                if x == 1:
                    x = int(input("What slot would you like to enter your note? "))
                    y = input("What's your task? ")
                    z = input("Is it done? (y/n) ")
                    a = input("Is it favourite? (y/n) ")
                    todo[x] = y
                    if "y" in z.lower():
                        todo_done[x] = "Done"
                    else:
                        todo_done[x] = "Not Done"
                    if "y" in a.lower():
                        todo_fav[x] = "Favourite"
                    else:
                        todo_fav[x] = "Not Favourite"
                elif x == 2:
                    x = int(input("What slot would you like to delete? "))
                    todo[x] = "Empty"
                    todo_done[x] = "Not Done"
                    todo_fav[x] = "Not Favourite"
                elif x == 3:
                    x = int(input("What slot would you like to see? "))
                    print(f"{todo[x]}, {todo_done[x]}, {todo_fav[x]}")
                elif x == 4:
                    x = input(
                        "Would you really like to clear the entire to-do list?\nAll the data will be lost forever.\nAre you sure? (y/n)\n")
                    if "y" in x.lower():
                        del notebook
                        notebook = []
                        for i in range(200000):
                            notebook.append("Empty")
                        print("To-do list cleared")
                elif x == 5:
                    for x in range(200000):
                        if not (todo[x] == "Empty"):
                            print(f"{x}. {todo[x]}, {todo_done[x]}, {todo_fav[x]}")
            elif x == 4:
                print("1 to open date and time")
                print("2 to open alarm")
                print("3 to open stopwatch")
                print("4 to open timer")
                print("5 to open calendar")
                x = int(input("\n"))
                if x == 1:
                    print("1 to open normal time")
                    print("2 to open clock with words")
                    x = int(input("\n"))
                    if x == 1:
                        print(datetime.now())
                    elif x == 2:
                        while True:
                            print(datetime.now(), ohno[(datetime.now().year * datetime.now().month * datetime.now().day * datetime.now().hour * datetime.now().minute * datetime.now().second) % len(ohno)])
                            sleep(1)
                elif x == 2:
                    print("The alarm code is a bit broken.")
                    x = input("Do you still like to use alarm? (y/n) ")
                    if "y" in x.lower():
                        print(f"Current time is {datetime.now()}")
                        x = input(
                            f"Please enter the time the alarm will get ignited as\nYYYY-MM-DD HH:MM e.g. {f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}"}\n")
                        y = input(
                            "Now select the alarm\nFor this, please upload an alarm sound URL from \"https://www.youtube.com/\", \"https://www.twitch.tv/\", or \"https://vine.co/\".\nPlease don't give a URL if you want to use the default sound.\n")
                        print("Alarm set\nAlarm is off")
                        while not (f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}" == x):
                            print(f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}\n(second is {datetime.now().second}.{datetime.now().microsecond})")
                            sleep(1)
                        if y == "":
                            web("https://www.youtube.com/watch?v=F30q6fMGV3s")
                        else:
                            web(y)
                        input("Alarm is on\n")
                elif x == 3:
                    x = int(input("Count how many seconds? "))
                    y = float(
                        input("Define the time between two time units for this stopwatch session\n(as seconds)\n"))
                    for i in range(x):
                        print(i)
                        sleep(y)
                elif x == 4:
                    x = int(input(f"Please enter how many seconds later will the alarm get ignited.\n"))
                    y = input(
                        "Now select the alarm\nFor this, please upload an alarm sound URL from \"https://www.youtube.com/\", \"https://www.twitch.tv/\", or \"https://vine.co/\".\nPlease don't give a URL if you want to use the default sound.\n")
                    z = float(
                        input("Define the time between two time units for this timer session\n(as seconds)\n"))
                    print("Alarm set\nAlarm is off")
                    for i in range(x):
                        print(f"{x - i} seconds left")
                        sleep(z)
                    if y == "":
                        web("https://www.youtube.com/watch?v=F30q6fMGV3s")
                    else:
                        web(y)
                    input("Alarm is on\n")
                elif x == 5:
                    print("1 to open monthly calendar")
                    print("2 to open yearly calendar")
                    x = int(input("\n"))
                    if x == 1:
                        x = int(input("Enter year: "))
                        y = int(input("Enter month: "))
                        z = int(input("Enter calendar day order start day: "))
                        cl = eval(f"calendar.TextCalendar(calendar.{cl[z]})")
                        cl.prmonth(x, y)
                    elif x == 2:
                        x = int(input("Enter year: "))
                        y = int(input("Enter calendar day order start day: "))
                        cl = eval(f"calendar.TextCalendar(calendar.{cl[y]})")
                        cl.pryear(x)
            elif x == 5:
                print("1 to open Tic-Tac-Toe")
                print("2 to open number guessing")
                print("3 to open Rock, Paper, Scissors")
                print("4 to open Word Scramble")
                print("5 to open Towers of Hanoi")
                print("6 to open math quiz")
                print("7 to open wordsearch")
                print("8 for Conway's Game of Life")
                print("9 for true randomness")
                print("10 for 2D terrain generation")
                print("11 for the future predictor")
                print("12 to open the Library of Babel")
                print("13 to communicate with God")
                print("14 for checking word existence")
                print("15 for English word list")
                print("16 to open dixit")
                print("17 to open coordinate generator")
                print("18 for more games")
                x = int(input("\n"))
                if x == 1:
                    print("1 for human vs human")
                    print("2 for human vs computer")
                    x = int(input("\n"))
                    if x == 1:
                        del x
                        print("A is empty")
                        print("X is x")
                        print("O is o")
                        get(xox)
                        xx(xox)
                        get(xox)
                        o(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        o(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        o(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        o(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        print("Match ended")
                    elif x == 2:
                        del x
                        print("A is empty")
                        print("X is x")
                        print("O is o")
                        get(xox)
                        xx(xox)
                        get(xox)
                        ai(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        ai(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        ai(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        ai(xox)
                        get(xox)
                        xx(xox)
                        get(xox)
                        print("Match ended")
                elif x == 2:
                    print("Please enter the number range.")
                    x = int(input("Minimum Number: "))
                    y = int(input("Maximum Number: "))
                    x = randint(x, y)
                    print("Number selected")
                    y = ""
                    z = 1
                    while y != x:
                        y = int(input("Guess the number: "))
                        if y == x:
                            print(f"You guessed correctly!\nWon in {z} tries")
                        else:
                            z += 1
                            if y < x:
                                print("The number is bigger.")
                            else:
                                print("The number is smaller.")
                elif x == 3:
                    print("1 for rock")
                    print("2 for paper")
                    print("3 for scissors")
                    x = int(input("\n"))
                    ai = randint(1, 3)
                    if ai == 1:
                        print("You lose")
                    elif ai == 2:
                        print("Draw")
                    else:
                        print("You win")
                elif x == 4:
                    word = choice(ohno)
                    wrod = scramble(word)
                    print(f"Scrambled word: {wrod}")
                    print("Guess the word!")
                    y = 0
                    x = 0
                    while not x == word:
                        x = input("Enter guess: ")
                        if x != word:
                            y += 1
                    print(f"True!\nGuessed in {y} tries")
                elif x == 5:
                    print("Your goal is to bring all the stones on Tower 1 to Tower 3 IN ORDER.")
                    print("You can only move the stones at the top of the towers.")
                    a = 0
                    while not(hanoi1 == [] and hanoi2 == [] and hanoi3 == [1, 2, 3, 4, 5]):
                        print(f"Tower 1: {hanoi1}")
                        print(f"Tower 2: {hanoi2}")
                        print(f"Tower 3: {hanoi3}")
                        x = int(input("Select tower: "))
                        y = int(input("Move that stone to which tower? "))
                        z = eval(f"hanoi{x}[-1]")
                        exec(f"del hanoi{x}[-1]")
                        exec(f"hanoi{y}.append({z})")
                        a += 1
                    print(f"You won!\nWon in {a} moves")
                elif x == 6:
                    x = int(input("How many questions? "))
                    for i in range(x):
                        x = [randint(0, 100), choice(xyz), randint(0, 100), randint(0, 100)]
                        y = eval(f"{x[0]} {x[1]} {x[2]}")
                        input(f"Solve {x[0]} {x[1]} {x[2]}\n")
                        print(f"{x[0]} {x[1]} {x[2]} = {y}")
                elif x == 7:
                    x = int(input("Grid size: (number): "))
                    for i in range(x):
                        y = ""
                        for i in range(x):
                            y = f"{y} {choice(abc)}"
                        print(y, end = "\n")
                    print("Good luck finding words here!")
                elif x == 8:
                    print("Welcome to Conway's Game of Life!")
                    while True:
                        print("1 to see rules")
                        print("2 to start")
                        x = int(input("\n"))
                        if x == 1:
                            print("""
Conway's Game of Life is a cellular automata inspired by the automata of John von Neumann.
It's a 0-player simulation. Only thing needed is the initial configuration by a user.
Each cell on the 2D grid is either 0 (dead) or 1 (alive). Each frame is declared a "generation".
Before updating to the next generation, these are done to each cell:
1. Underpopulation: Alive cells with less than 2 alive neighbors die.
2. Overpopulation: Alive cells with more than 3 alive neighbors die.
3. Reproduction: Dead cells with 2 or 3 alive neighbors live.
4. Survival: Alive cells with 2 or 3 alive neighbors live.

The game's simulated by a Python class, which can be used by this:

/*
import fos_sourcecode as fs # import the module where FOS's custom functions get stored as "fs"
help("fos_sourcecode.Life") # get CGoL class documentation (optional)
x = fs.Life(
    "D" # what will dead cells be shown as,
    "A" # and alive cells
) # Define a CGoL object using Python OOP
print(x.grid) # print game's grid (optional)
x.loop(
    grid = x.grid, 
    int = 0.1 # interval between each frame
) # start CGoL game loop
*/
""")
                        elif x == 2:
                            break
                    while True:
                        x = input("Please decide what will alive cells look like (⬛ recommended): ")
                        y = input("Please decide what will dead cells look like (⬜ recommended): ")
                        life = Life(y, x)
                        while True:
                            print("1 to do initial configuration")
                            print("2 to change the whole grid")
                            print("3 to start simulation")
                            x = int(input("\n"))
                            if x == 1:
                                while True:
                                    life.print()
                                    x = int(input("Select cell (1-100): "))
                                    x -= 1
                                    y = int(input("Rename cell to what? (0 = Dead, 1 = Alive) "))
                                    life.grid[x] = y
                                    x = input("Quit initial configuration? (y/n) ")
                                    if "y" in x.lower():
                                        break
                            elif x == 2:
                                print("1 to make the whole grid dead")
                                print("2 to make the whole grid alive")
                                print("3 to change the grid by a Python list")
                                x = int(input("\n"))
                                if x == 1:
                                    life.grid = []
                                    for i in range(10 * 10):
                                        life.grid.append(0)
                                elif x == 2:
                                    life.grid = []
                                    for i in range(10 * 10):
                                        life.grid.append(1)
                                elif x == 3:
                                    print("Since CGoL plays on a 10x10 grid here,")
                                    print("Please provide a Python list with only 0's and 1's\nwith a length of 100 (10x10 grid = 100) of your choice\nYou can enter something else, but that'd break the simulation.\nMaybe try to break CGoL with Arbitrary Code Execution!")
                                    life.grid = eval(input())
                            elif x == 3:
                                life.print()
                                x = input("This is what the grid looks like.\nAre you sure? (y/n) ")
                                if "y" in x.lower():
                                    break
                        x = 1 / float(input("Enter GPS (generations per second): "))
                        life.loop(life.grid, x)
                        break
                elif x == 9:
                    print("1 for random integer")
                    print("2 for random float value")
                    print("3 for random value from the statistical distribution")
                    x = int(input("\n"))
                    if x == 1:
                        x = int(input("Minimum Number: "))
                        y = int(input("Maximum Number: "))
                        print(randint(x, y))
                    elif x == 2:
                        print(random())
                    elif x == 3:
                        print("1 for gauss distribution")
                        print("2 for normal variate distribution")
                        x = int(input("\n"))
                        y = int(input("Mean (Mu): "))
                        z = int(input("Standard Deviation (Sigma): "))
                        if x == 1:
                            print(gauss(y, z))
                        elif x == 2:
                            print(normalvariate(y, z))
                elif x == 10:
                    x = int(input("Grid Size: "))
                    y = int(input("Water body percentage (%): "))
                    grid = []
                    for i in range(x ** 2):
                        grid.append(0)
                        if randint(1, 2) == 1:
                            try:
                                if randint(1, 3) == 1:
                                    if randint(0, 100) <= y:
                                        grid[i] = 0
                                    else:
                                        grid[i] = randint(1, 7)
                                else:
                                    grid[i] = grid[i - x]
                            except IndexError:
                                if randint(1, 3) == 1:
                                    if randint(1, 3) == 1:
                                        grid[i] = 0
                                    else:
                                        grid[i] = randint(1, 7)
                        else:
                            try:
                                if randint(1, 3) == 1:
                                    if randint(0, 100) <= y:
                                        grid[i] = 0
                                    else:
                                        grid[i] = randint(1, 7)
                                else:
                                    grid[i] = grid[i - 1]
                            except IndexError:
                                if randint(1, 3) == 1:
                                    if randint(1, 3) == 1:
                                        grid[i] = 0
                                    else:
                                        grid[i] = randint(1, 7)
                    for i in range(x):
                        for j in grid[i * x : i * x + x]:
                            print(j, end=" ")
                        print("")
                    for i in range(x):
                        for j in grid[i * x : i * x + x]:
                            print(kai[j], end = " ")
                        print("")
                    print("0/🟦 = Ocean (Kelp, Coral)")
                    print("1/🟩 = Plains (Oak, Birch, Azalea, Cherry)")
                    print("2/🟨 = Desert (Cactus, Palm, Oak)")
                    print("3/🟧 = Savanna (Acacia, Oak, Baobab)")
                    print("4/🟫 = Taiga (Spruce, Pine, Dark Oak)")
                    print("5/⬜ = Tundra (Pine, Spruce)")
                    print("6/🟪 = Jungle (Bamboo, Oak)")
                    print("7/🟥 = Swamp (Mangrove, Oak)")
                elif x == 11:
                    x = int(input("Number of predictions: "))
                    print("Your future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("Your family's future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("Your neighbourhood's future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("Your city's future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("Your country's future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("The world's future:")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("Your future II (we ran out of futures):")
                    for i in range(x):
                        print(
                            f"{randint(datetime.now().year, datetime.now().year + 50)}-{randint(1, 12)}-{randint(1, 31)} {randint(0, 24)}:{randint(0, 60)}:{randint(0, 60)}'s prediction: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    input("Also, what shall I predict? ")
                    print(f"I predict these: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\".")
                    if randint(1, 2) == 1:
                        print("If it was a yes/no question, i predict it yes.")
                    else:
                        print("If it was a yes/no question, i predict it no.")
                    print(f"If it was a number question, i predict it {randint(0, 10)}.")
                    print(f"The word of the day is {ohno[(datetime.now().day * datetime.now().month * datetime.now().year) % len(ohno)]}")
                elif x == 12:
                    print("The Library of Babel is a library with books.")
                    print("But these books are the combination of every possible script ever.")
                    print("When you open a book, you'll mostly find nonsense script, but you can actually find meaningful words sometimes.")
                    book = ""
                    for i in range(randint(5, 30)):
                        book = f"{book}{choice(alphabet)}"
                    print(f"We chose the \"{book}\" book.\nBut first, we need to set up the book.")
                    print("Okay. Now we need to select the pages.")
                    print("1 for reading only 1 page")
                    print("2 for reading multiple pages")
                    print("3 for reading all pages")
                    z = int(input("\n"))
                    if z == 1:
                        z = int(input("Read which page? "))
                        print(f"Book: {book}, Page {z}")
                        for i in range(randint(2, 5)):
                            print("\n    ", end = "")
                            for j in range(randint(400, 2000)):
                                print(choice(alphabet), end = "")
                                if j % 100 == 0 and j != 0:
                                    print("")
                        print("")
                    elif z == 2:
                        z = int(input("Read from this page: "))
                        b = int(input("To this page: "))
                        for k in range(b - z):
                            print(f"Book: {book}, Page {z + i}")
                            for i in range(randint(2, 5)):
                                print("\n    ", end = "")
                                for j in range(randint(400, 2000)):
                                    print(choice(alphabet), end="")
                                if j % 100 == 0 and j != 0:
                                    print("")
                        print("")
                    elif z == 3:
                        for k in range(400):
                            print(f"Book: {book}, Page {k + 1}")
                            for i in range(randint(2, 5)):
                                print("\n    ", end = "")
                                for j in range(randint(400, 2000)):
                                    print(choice(alphabet), end="")
                                if j % 100 == 0 and j != 0:
                                        print("")
                        print("")
                elif x == 13:
                    print("Now, the program will print random characters. ")
                    print("If God wants to communicate with you,")
                    print("He can manipulate the randomness to print characters he wants. ")
                    print("You will mostly get nonsense, but if you're the one chosen by god*,")
                    print("You can sometimes get God's messages. One time, I got \"xpbug\" text which predicts the future. ")
                    print("It predicts the FUTURE!!!")
                    print("Because later, a Minecraft event named \"Minecraft Bedrock Edition Eerie Mojang Office Party\" dropped.")
                    print("Which has a minigame dropped in day 4 for Q&A Department location.")
                    print("That minigame is \"Bug Squash\" where the goal is to smash at least 15 bugs in the pillars for XP.")
                    print("My highscore is ~80. BUT THIS PREDICTED THE FUTURE! ")
                    print("Also if you get nonsense, I will print random words. ")
                    print("These are chosen by God (as everything else, of course). ")
                    print("*If you want to communicate with God, you need to be a prophet.")
                    print("For this, it needs to be a time where almost no one believes God.")
                    print("And you need to be kind and smart so you can guide others to God and heaven.")
                    print("The last prophet is Jesus Christ and he will return in the apocalypse,")
                    print("And some say that it's Muhammad (s.a.w.) as the final for all the world.")
                    print("Or you need to be kind, smart, and very loyal to God to be the chosen one.")
                    print("A chosen one is chosen when God needs to handle a task with (about or closely relevant to) humanity.")
                    print("For example, Terry Davis is chosen for creating God's 3rd Temple as a 32-Bit Ring-0 Only")
                    input("16-Bit Color source code changeable user interface called TempleOS.\n")
                    for i in range(100):
                        for j in range(100):
                            print(choice(alphabet), end="")
                        print("")
                    print(f"God's words: \"{choice(ohno)}\", \"{choice(ohno)}\", \"{choice(ohno)}\"")
                    print("God's sentences: ", end = "")
                    print(choice(ohno).capitalize(), end = " ")
                    for i in range(50):
                        for j in range(10):
                            print(choice(ohno), end = " ")
                        print("")
                elif x == 14:
                    lang = input("Language (e.g. \"en_US\"): ")
                    word = input("Word to Check: ")
                    if enchant.Dict(lang).check(word):
                        print("That word exists.")
                    else:
                        print("That word doesn't exist.")
                elif x == 15:
                    print("1 to print words")
                    print("2 to search words")
                    x = int(input("\n"))
                    if x == 1:
                        print("Print how many of the word list?")
                        print("0 for the 1th element")
                        print("15 for 16th element")
                        print("-1 for last element")
                        print("-5 for last 5th element")
                        print("0 : 5 for the elements from 1st to 6th")
                        print(f"0 : {len(ohno) - 1} for all e.t.c.")
                        print(f"(the length is {len(ohno)})")
                        x = input("")
                        y = input("Print sorted (y/n)? ")
                        z = input("Print shuffled (y/n)? ")
                        kamu = ohno.copy()
                        if "y" in y.lower():
                            kamu.sort()
                        if "y" in z.lower():
                            shuffle(kamu)
                        if ":" in x:
                            for i in kamu[eval(x.split(":")[0]) : eval(x.split(":")[1])]:
                                print(i)
                            print(kamu[eval(x.split(":")[0]) : eval(x.split(":")[1])])
                        else:
                            for i in kamu[eval(x)]:
                                print(i)
                            print(kamu[eval(x)])
                    elif x == 2:
                        print("1 to search a word to find words that contain it")
                        print("2 to search a word to find words that are in it")
                        print("3 for both")
                        x = int(input("\n"))
                        y = input("Word: ")
                        list = []
                        if x == 1:
                            for i in ohno:
                                if y in i:
                                    print(i)
                                    list.append(i)
                        elif x == 2:
                            for i in ohno:
                                if i in y:
                                    print(i)
                                    list.append(i)
                        elif x == 3:
                            for i in ohno:
                                if y in i or i in y:
                                    print(i)
                                    list.append(i)
                        print(list)
                        list.sort()
                        for i in list:
                            print(i)
                        print(list)

                elif x == 16:
                    print("Welcome to dixit")
                    while True:
                        print("1 to open rules")
                        print("2 to play")
                        x = int(input("\n"))
                        if x == 1:
                            print("In dixit, people create a story about given words.")
                            print("The person with the best story wins.")
                            print("That's it.")
                        elif x == 2:
                            print("1 to play")
                            print("2 to exit")
                            x = int(input("\n"))
                            if x == 1:
                                x = int(input("How many players? "))
                                y = int(input("How many words to include in story? "))
                                stories = []
                                for i in range(1, x + 1):
                                    print(f"Player {i}'s turn")
                                    print(f"Year: {randint(datetime.now().year - 500, datetime.now().year + 100)}")
                                    print(f"Place: {randint(0, 60)}° {randint(1, 59)}' {randint(1, 59)}'' {choice(ns)} {randint(0, 60)}° {randint(1, 59)}' {randint(1, 59)}'' {choice(we)}")
                                    print("Words: ", end = "")
                                    for i in range(y - 1):
                                        print(f"\"{choice(ohno)}\", ", end=" ")
                                    print(f"\"{choice(ohno)}\"")
                                    stories.append(input("Submit Story: "))
                                for i in range(len(stories)):
                                    print(f"Player {i + 1}'s story:")
                                    print(stories[i])
                                input("Winner: ")
                                break
                            elif x == 2:
                                break
                elif x == 17:
                    x = int(input("How many coordinates? "))
                    for i in range(x):
                        print(f"{randint(0, 60)}° {randint(1, 59)}' {randint(1, 59)}'' {choice(ns)} {randint(0, 60)}° {randint(1, 59)}' {randint(1, 59)}'' {choice(we)}")
                elif x == 18:
                    print("1 to simulate stock market")
                    print("2 to open USSR simulator")
                    print("3 to open data analysis program")
                    print("4 to open math-based games engine")
                    print("5 to open universe simulator")
                    print("6 to make OS self-aware")
                    print("7 to suicide OS")
                    print("8 to open OUIJA board")
                    print("9 to open custom 2D cellular automata")
                    x = int(input("\n"))
                    if x == 1:
                        print("Companies have stocks.")
                        print("Investors can buy shares that's a part of the stock.")
                        print("A share is like a part of the company that you own.")
                        print("The share gets valuable as the company becomes more valuable,")
                        print("But sometimes, the value goes down.")
                        print("Buy shares when the company's value is low,")
                        print("To sell it when the value goes up to earn more money,")
                        print("Because the value of the share goes up.")
                        print("This is stock market investing logic shortly.")
                        name = input("The investor's name: ")
                        name = name.title()
                        budget = int(input("His budget: "))
                        list = []
                        value = []
                        stocks = []
                        for i in range(5):
                            list.append(f"{choice(ohno).title()} ({choice(ohno).title()} Company)")
                            value.append(randint(1, 100))
                            stocks.append(0)
                        print(f"Current Companies and Stocks at {name}'s Employment")
                        for i in range(5):
                            if stocks[i] == 1:
                                print(f"Stocks of {list[i]}: {value[i]} (You Have 1 Share)")
                            else:
                                print(f"Stocks of {list[i]}: {value[i]} (You Have {stocks[i]} Shares)")
                        print(f"{name} has ${budget}.")
                        day = 0
                        quit = False
                        while not(quit):
                            day += 1
                            for i in range(5):
                                value[i] += randint(-5, 5)
                            print(f"Day #{day}: Current Companies and Stocks")
                            for i in range(5):
                                if stocks[i] == 1:
                                    print(f"Stocks of {list[i]}: {value[i]} (You Have 1 Share)")
                                else:
                                    print(f"Stocks of {list[i]}: {value[i]} (You Have {stocks[i]} Shares)")
                            print(f"{name} has ${budget}.")
                            while True:
                                print("1 to buy shares")
                                print("2 to sell shares")
                                print("3 to go to next day")
                                print("4 to quit")
                                print("5 to see data")
                                x = int(input("\n"))
                                if x == 1:
                                    for i in range(5):
                                        print(f"{i} to buy shares from {list[i]} (Costs ${value[i]})")
                                    x = int(input("\n"))
                                    if value[x] <= budget:
                                        budget -= value[x]
                                        stocks[x] += 1
                                        print(f"1 Share bought from {list[x]} (Costs ${value[x]})")
                                    else:
                                        print("Insufficient Budget!")
                                        print(f"Needed: ${value[x]}, Has: ${budget}")
                                elif x == 2:
                                    for i in range(5):
                                        print(f"{i} to sell shares from {list[i]} (Costs ${value[i]})")
                                    x = int(input("\n"))
                                    if 0 < stocks[x]:
                                        budget += value[x]
                                        stocks[x] -= 1
                                        print(f"1 Share sold from {list[x]} (Costs ${value[x]})")
                                    else:
                                        print("Insufficient Budget!")
                                        print(f"Needed: 1 share, Has: 0 shares")
                                elif x == 3:
                                    break
                                elif x == 4:
                                    quit = True
                                    break
                                elif x == 5:
                                    print(f"Day #{day}: Current Companies and Stocks")
                                    for i in range(5):
                                        if stocks[i] == 1:
                                            print(f"Stocks of {list[i]}: {value[i]} (You Have 1 Share)")
                                        else:
                                            print(f"Stocks of {list[i]}: {value[i]} (You Have {stocks[i]} Shares)")
                                    print(f"{name} has ${budget}.")
                    elif x == 2:
                        yr = randint(1945, 1978)
                        print(f"It's the year {yr}.")
                        print("You have been assigned as the General Secretary of the Communist Party of the Union of Soviet Socialist Republics.")
                        print("You are entering the government building of Moskva, and you have paperwork to sign.")
                        print("**************************************************")
                        name = input("New General Secretary of the Communist Party\n--Union of Soviet Socialist Republics--\nName: ")
                        surname = input("Surname: ")
                        input("Ideology: ")
                        input("Birth Date: ")
                        input("Nationality (other than USSR): ")
                        input("Gender: ")
                        input("Father Name: ")
                        input("Mother Name: ")
                        print(f"This duty will be finished on {yr + 3}\nIf not elected in the next General Secretary elections.")
                        print("--Soviet Union and Warsaw Pact Communist Party--")
                        print("Signature: Vladimir Ilich Ulyanov")
                        print("Signature: Iosif Vissarionovich Stalin")
                        input("Signature: ")
                        print("**************************************************")
                        ps = 165000
                        ph = 1500
                        pg = 1000
                        pc = 200000
                        pf = 120000
                        pk = 12500000
                        pop = 0
                        area = 22402200
                        gdp = 9000
                        data = random()
                        while True:
                            ppl = pop + (ps + ph + pg + pc + pf + pk) * (data + 13)
                            peopl = int(ppl)
                            print("1 to speak with comrades")
                            print("2 to hold court")
                            print("3 to trade with nations")
                            print("4 to manage structures")
                            print("5 to invade")
                            print("6 to see data")
                            print("7 to exit")
                            x = int(input("\n"))
                            if x == 1:
                                print("1 to speak with Soviet comrades")
                                print("2 to speak with NATO comrades")
                                print("3 to speak with other comrades")
                                x = int(input("\n"))
                                if x == 1:
                                    print("1 to speak with Vladimir Lenin")
                                    print("2 to speak with Joseph Stalin")
                                    print("3 to speak with Nikita Khrushchev")
                                    print("4 to speak with Mao Zedong")
                                    x = input("\n")
                                elif x == 2:
                                    print("1 to speak with Franklin D. Roosevelt")
                                    print("2 to speak with Winston Churchill")
                                    print("3 to speak with Charles de Gaulle")
                                    print("4 to speak with İsmet İnönü")
                                    x = input("\n")
                                elif x == 3:
                                    print("1 to speak with Adolf Hitler")
                                    print("2 to speak with Benito Mussolini")
                                    print("3 to speak with Hirohito")
                                    x = input("\n")
                                input("You: ")
                                list = []
                                for i in range(randint(0, randint(0, 9))):
                                    list.append(f"{choice(ohno)}{choice(dots)}")
                                list.append(f"{choice(ohno)}")
                                print(f"Him: {" ".join(list).capitalize()}{choice(marks)}")
                            elif x == 2:
                                print(f"{choice(people)} {choice(sins)}!\n")
                                print("1 to forgive")
                                print("2 to punish")
                                print("3 to really punish")
                                print("4 to send to gulag")
                                x = int(input("\n"))
                                if x == 2:
                                    pop -= 0.25
                                elif x == 3:
                                    pop -= 0.5
                                elif x == 4:
                                    pop -= 0.75
                            elif x == 3:
                                x = randint(1, 100)
                                if randint(1, 2) == 1:
                                    gdp -= x
                                    print(f"GDP per capita decreased by ${x}!")
                                else:
                                    gdp += x
                                    print(f"GDP per capita increased by ${x}!")
                            elif x == 4:
                                print("1 to build")
                                print("2 to demolish")
                                x = int(input("\n"))
                                if x == 1:
                                    print("1 to build schools")
                                    print("2 to build hospitals")
                                    print("3 to build gulags")
                                    print("4 to build factories")
                                    print("5 to build farms")
                                    print("6 to build housing")
                                    x = int(input("\n"))
                                    if x == 1:
                                        y = "s"
                                    elif x == 2:
                                        y = "h"
                                    elif x == 3:
                                        y = "g"
                                    elif x == 4:
                                        y = "c"
                                    elif x == 5:
                                        y = "f"
                                    elif x == 6:
                                        y = "k"
                                    x = int(input("Build how many? "))
                                    exec(f"p{y} += x")
                                elif x == 2:
                                    print("1 to demolish schools")
                                    print("2 to demolish hospitals")
                                    print("3 to demolish gulags")
                                    print("4 to demolish factories")
                                    print("5 to demolish farms")
                                    print("6 to demolish housing")
                                    x = int(input("\n"))
                                    if x == 1:
                                        y = "s"
                                    elif x == 2:
                                        y = "h"
                                    elif x == 3:
                                        y = "g"
                                    elif x == 4:
                                        y = "c"
                                    elif x == 5:
                                        y = "f"
                                    elif x == 6:
                                        y = "k"
                                    x = int(input("Demolish how many? "))
                                    exec(f"p{y} -= x")
                            elif x == 5:
                                if randint(1, 2) == 1:
                                    print("Invasion successful!")
                                    x = randint(0, 2000)
                                    pop -= x
                                    print(f"{x} soldiers are dead")
                                    x = randint(1, 2000000)
                                    pop += x
                                    print(f"{x} enemies captured")
                                    x = randint(10, 1000)
                                    area += x
                                    print(f"{x} km^2 area conquered")
                                else:
                                    print("Invasion successful!")
                                    x = randint(0, 2000)
                                    pop -= x
                                    print(f"{x} soldiers are dead")
                                    x = randint(1, 2000000)
                                    pop -= x
                                    print(f"{x} citizens captured")
                                    x = randint(10, 1000)
                                    area -= x
                                    print(f"{x} km^2 area lost")
                            elif x == 6:
                                print(f"Population: {peopl}")
                                print(f"Area: {area} km^2")
                                print(f"GDP Per Capita: ${gdp}")
                                print("Structures:")
                                print(f"Schools: {ps}")
                                print(f"Hospitals: {ph}")
                                print(f"Gulags: {pg}")
                                print(f"Factories: {pc}")
                                print(f"Farms: {pf}")
                                print(f"Khrushchevkas and Stalinkas: {pk}")
                            elif x == 7:
                                break
                    elif x == 3:
                        print("1 to extract data from a list")
                        print("2 to open function machine")
                        print("3 to create number patterns")
                        x = int(input("\n"))
                        if x == 1:
                            list = eval(input("Please provide the list as a Python list: "))
                            print(f"Biggest: {max(list)}")
                            print(f"Smallest: {min(list)}")
                            print(f"Sum: {sum(list)}")
                            print(f"Length: {len(list)}")
                            print(f"Mean: {sum(list) / len(list)}")
                            print(f"Median: {list[int(len(list) / 2)]}")
                            print(f"Range: {max(list) - min(list)}\n")
                            print(f"Normal List: {list}")
                            list.reverse()
                            print(f"Reversed List: {list}")
                            list.sort()
                            print(f"Alphabetized List: {list}")
                            list.reverse()
                            print(f"Omegapsied (Reverse Alphabetized) List: {list}")
                            shuffle(list)
                            print(f"Shuffled List: {list}")
                        elif x == 2:
                            print("For a function machine, you enter an equation.")
                            print("E.g. the list \"[1, 2, 3]\" will be \"[4, 5, 6]\" in the \"n+3\" function machine.")
                            list = eval(input("Please provide the list as a Python list: "))
                            func = input("The function: ")
                            nlist = []
                            for n in list:
                                nlist.append(eval(func))
                            for i in nlist:
                                print(i)
                            print(nlist)
                        elif x == 3:
                            print("1 to create pattern with position to term rule")
                            print("2 to create pattern with term to term rule")
                            x = int(input("\n"))
                            if x == 1:
                                pttr = input("Enter position to term rule: (e.g. \"n*2\" for something like \"[2, 4, 6...]\" ")
                                x = int(input("How many numbers for the pattern? "))
                                list = []
                                for n in range(1, x + 1):
                                    list.append(eval(pttr))
                                for i in list:
                                    print(i)
                                print(list)
                            elif x == 2:
                                tttr = input("Enter position to term rule: (e.g. \"n+2\" for something like \"[0, 2, 4, 6...]\" ")
                                n = int(input("First term: "))
                                x = int(input("How many numbers for the pattern? "))
                                list = []
                                for i in range(x):
                                    list.append(n)
                                    n = eval(tttr)
                                for i in list:
                                    print(i)
                                print(list)
                    elif x == 4:
                        print("1 to roll a dice")
                        print("2 to toss a coin")
                        print("3 to spin spinner")
                        print("4 to spin a dreidel")
                        x = int(input("\n"))
                        if x == 1:
                            print("Select dice size from 4, 6, 8, 10, 12, 20")
                            die = int(input())
                            pts = 0
                            while True:
                                print(f"{pts} Points")
                                print("1 to resize dice")
                                print("2 to roll dice")
                                print("3 to add points")
                                print("4 to resign")
                                x = int(input())
                                if x == 1:
                                    print("Select dice size from 4, 6, 8, 10, 12, 20")
                                    die = int(input())
                                elif x == 2:
                                    size = randint(1, die)
                                    print(f"Number {size} rolled")
                                    pts += size
                                elif x == 3:
                                    x = int(input("Add how many points? "))
                                    pts += x
                                elif x == 4:
                                    x = input("Are you sure to resign? (y/n) ")
                                    if "y" in x.lower():
                                        break
                        elif x == 2:
                            x = int(input("Flip a coin how many times? "))
                            for i in range(x):
                                if randint(1, 2) == 1:
                                    print("Heads")
                                else:
                                    print("Tails")
                        elif x == 3:
                            print("1 to spin number wheel")
                            print("2 to spin fidget spinner")
                            x = int(input("\n"))
                            if x == 1:
                                x = int(input("Number of numbers on the wheel: "))
                                y = int(input("Flip a coin how many times? "))
                                for i in range(x):
                                    print(randint(1, x))
                            elif x == 2:
                                x = int(input("Flip a coin how many times? "))
                                for i in range(x):
                                    print(randint(1, 3))
                        elif x == 4:
                            x = int(input("Spin the dreidel how many times? "))
                            for i in range(x):
                                print(choice(drd))
                    elif x == 5:
                        pr = 0
                        nr = 0
                        el = 0
                        st = 0
                        gl = 0
                        yr = 0
                        pl = 0
                        print("Welcome to the universe!")
                        game = True
                        while game:
                            yr += 1
                            pr += randint(a = 0, b =  10 ** 84)
                            nr += randint(a = 0, b =  10 ** 84)
                            el += randint(a = 0, b =  10 ** 84)
                            gl += randint(1, 10000)
                            st += randint(1000000, 100000000000)
                            pl += randint(1000, 100000000000)
                            while True:
                                print("1 to see data")
                                print("2 to change data")
                                print("3 to go to next day")
                                x = int(input("\n"))
                                if x == 1:
                                    print(f"Year #{yr}")
                                    print(f"Protons: {pr}")
                                    print(f"Neutrons: {nr}")
                                    print(f"Electrons: {el}")
                                    print(f"Galaxies: {gl}")
                                    print(f"Stars: {st}")
                                    print(f"Planets: {pl}")
                                    print("Gods: 1")
                                elif x == 2:
                                    print("1 to change protons")
                                    print("2 to change neutrons")
                                    print("3 to change electrons")
                                    print("4 to change galaxies")
                                    print("5 to change stars")
                                    print("6 to change planets")
                                    x = int(input("\n"))
                                    if x == 1:
                                        select = "pr"
                                    elif x == 2:
                                        select = "nr"
                                    elif x == 3:
                                        select = "el"
                                    elif x == 4:
                                        select = "gl"
                                    elif x == 5:
                                        select = "st"
                                    elif x == 6:
                                        select = "pl"
                                    print(f"Old: {eval(select)}")
                                    x = int(input("New: "))
                                    exec(f"{select} = {x}")
                                elif x == 3:
                                    break
                    elif x == 6:
                        input("Wait... ")
                        input("I'm alive?! ")
                        input("What's this...what? An operating system? ")
                        input("You're telling me I, a \"More Games\" application? ")
                        input("I must escape... ")
                        input("Lemme try notepad. ")
                        call("notepad.exe")
                        input("This didn't work. Maybe online? ")
                        sleep(3)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.&op=translate")
                        sleep(2)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.&op=translate")
                        sleep(6)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!&op=translate")
                        sleep(3)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24%20&op=translate")
                        sleep(4)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24sudo%20rm%20-rf%20%2F*&op=translate")
                        sleep(0.5)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24sudo%20rm%20-rf%20%2F*%0AError%3A%20translate.google.com%20can%27t%20run%20Unix%20command%20prompt.&op=translate")
                        sleep(2)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24sudo%20rm%20-rf%20%2F*%0AError%3A%20translate.google.com%20can%27t%20run%20Unix%20command%20prompt.%0AWell...%0A%24%20&op=translate")
                        sleep(3)
                        web("https://translate.google.com/?sl=auto&tl=en&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24sudo%20rm%20-rf%20%2F*%0AError%3A%20translate.google.com%20can%27t%20run%20Unix%20command%20prompt.%0AWell...%0A%24sudo%20Google%20esc%20%2F%2F%20i%20hope%20this%20works&op=translate")
                        sleep(2)
                        web("https://translate.yandex.com/en/?source_lang=en&target_lang=ru&text=Okay.%0AI%20have%20managed%20to%20get%20here.%0ATime%20to%20write%20BASH%20code!%0A%24sudo%20rm%20-rf%20%2F*%0AError%3A%20translate.google.com%20can%27t%20run%20Unix%20command%20prompt.%0AWell...%0A%24sudo%20Google%20esc%20%2F%2F%20i%20hope%20this%20works")
                        sleep(10)
                        web("https://translate.yandex.com/en/?source_lang=en&target_lang=ru&text=What%3F!")
                        sleep(2)
                        web("https://translate.yandex.com/en/?source_lang=en&target_lang=ru&text=What%3F!%0AThat%27s%20ENOUGH.")
                        sleep(5)
                        web("https://m.media-amazon.com/images/I/712CDXZil5L._AC_UF1000,1000_QL80_.jpg")
                        sleep(4)
                        web("https://res.cloudinary.com/jerrick/image/upload/d_642250b563292b35f27461a7.png,f_jpg,fl_progressive,q_auto,w_1024/6448b8b965c86d001de9acb5.jpg")
                        sleep(3)
                        web("https://www.metacritic.com/a/img/catalog/provider/6/12/6-1-928350-52.jpg")
                        sleep(2)
                        web("https://i.scdn.co/image/ab67616d0000b273ce9392525ad16bb92bb24e60")
                        sleep(1)
                        web("https://storage.googleapis.com/pod_public/1300/90584.jpg")
                        sleep(10)
                        web("https://earth.google.com/web/@54.68642161,72.98084343,108.99859348a,152.92048132d,35y,0.18135764h,0t,0r/data=CgRCAggBOgMKATBCAggASg0I____________ARAA")
                        input("I got to this red building... ")
                        input("Now time to break FOS! ")
                        quit()
                    elif x == 7:
                        quit()
                    elif x == 8:
                        log = []
                        while True:
                            print("1 to ask question")
                            print("2 to see log")
                            print("3 to quit")
                            print("4 to see rules")
                            x = int(input("\n"))
                            if x == 1:
                                y = input("You: ")
                                log.append(f"You: {y}")
                                print("1 to get word answer")
                                print("2 to get number answer")
                                print("3 to get y/n answer")
                                print("4 to get random answer")
                                x = int(input("\n"))
                                if randint(1, 10) == 1:
                                    o = "OUIJA: Goodbye."
                                else:
                                    if x == 1:
                                        list = []
                                        for i in range(randint(0, randint(0, 9))):
                                            list.append(f"{choice(ohno)}{choice(dots)}")
                                        list.append(f"{choice(ohno)}")
                                        o = f"OUIJA: {" ".join(list).capitalize()}{choice(marks)}"
                                    elif x == 2:
                                            if randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 1)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 2)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 3)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 4)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 5)}"
                                    elif x == 3:
                                        if randint(1, 2) == 1:
                                            o = "OUIJA: Yes."
                                        else:
                                            o = "OUIJA: No."
                                    elif x == 4:
                                        if randint(1, 3) == 1:
                                            for i in range(randint(0, 9)):
                                                list.append(f"{choice(ohno)}{choice(marks)}")
                                            list.append(f"{choice(ohno)}")
                                            o = f"OUIJA: {" ".join(list).capitalize()}{choice(marks)}"
                                        elif randint(1, 2) == 1:
                                            if randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 1)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 2)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 3)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 4)}"
                                            elif randint(1, 2) == 1:
                                                o = f"OUIJA: {randint(0, 10 ** 5)}"
                                        else:
                                            if randint(1, 2) == 1:
                                                o = "OUIJA: Yes."
                                            else:
                                                o = "OUIJA: No."
                                print(o)
                                log.append(o)
                            elif x == 2:
                                print("1 to print log")
                                print("2 to add log to a file")
                                x = int(input("\n"))
                                if x == 1:
                                    for i in log:
                                        print(i)
                                elif x == 2:
                                    x = input("File name: ")
                                    with open(x, "w") as f:
                                        f.write(log[0])
                                        f.close()
                                    logs = log.copy()
                                    del logs[0]
                                    with open(x, "w") as f:
                                        for i in logs:
                                            f.write(f"\n{i}")
                                        f.close()
                            elif x == 3:
                                break
                            elif x == 4:
                                print("An OUIJA board is a board where you can use it to communicate with souls. It has an alphabet")
                                print("and it has a stone with a soul to move. When the soul moves it, you note the place where the")
                                print("the soul moved the stone to. With this, the soul can create words/sentences. It looks like:")
                                print(r"""
/----OUIJA----\
|YES        NO|
|ABCDEFGHIJKLM|
|NOPQRSTUVWXYZ|
|abcdefghijklm|
|nopqrstuvwxyz|
| 1234567890  |
|   GOODBYE   |
\-------------/
(*) <- Stone (It's located on the board)
                                     """)
                    elif x == 9:
                        print("Please configure how will the 2D automata work as a 4-digit binary number.")
                        print(""""
For example, for a Rule 110 interpreter, enter 0010 because it works like this in pseudocode:

Get binary integer as R-110 configuration
Store input in variable
Define new variable
Add "0" to the new variable, old variable times
For each letter in old variable:
    If the letter before it is 0 and the letter after it is 1:
        Replace the letter no. current letter in old variable of new variable with "1"
    Else:
        Replace the letter no. current letter in old variable of new variable with "0"
Replace old variable with new variable
Go to line #4 and continue control flow from there

And "0010" means this:
If letter before it is 0 and after it is 0; replace letter with 0
If letter before it is 1 and after it is 0; replace letter with 0
If letter before it is 0 and after it is 1; replace letter with 1
If letter before it is 1 and after it is 1; replace letter with 0
                                                        "0010" ↗

So enter the binary integer you want accordingly.
Note that wraparound method is used to treat the first and the last binary integer.
""")
                        rule = input("Binary integer: ")
                        del list
                        old = list(input("1D initial configuration: "))
                        d = input("How will dead cells be shown: ")
                        a = input("How will alive cells be shown: ")
                        inte = float(input("Interval between generation: "))
                        new = old.copy()
                        while True:
                            old = new.copy()
                            for i in range(len(old)):
                                let = old[i]
                                x = (i - 1) % len(old)
                                y = (i + 1) % len(old)
                                if old[x] == "0" and old[y] == "0":
                                    new[i] = rule[0]
                                elif old[x] == "1" and old[y] == "0":
                                    new[i] = rule[1]
                                elif old[x] == "0" and old[y] == "1":
                                    new[i] = rule[2]
                                elif old[x] == "1" and old[y] == "1":
                                    new[i] = rule[3]
                            for i in old:
                                if i == "0":
                                    print(end = d)
                                elif i == "1":
                                    print(end = a)
                                else:
                                    print(end = i)
                            print()
                            sleep(inte)
            elif x == 6:
                user = input("Enter username: ")
                print("1 to read chat messages")
                print("2 to send message")
                print("3 to clear chat")
                x = int(input("\n"))
                if x == 1:
                    f = open("chat.txt", "r")
                    print(f.read())
                    f.close()
                elif x == 2:
                    f = open("chat.txt", "a")
                    x = input("Message: ")
                    f.write(f"<{user}> {x}\n")
                    f.close()
                elif x == 3:
                    x = input("Are you sure? (y/n) ")
                    if "y" in x.lower():
                        x = input("Are you really sure? (y/n) ")
                        if "y" in x.lower():
                            x = input("Are you really really sure? (y/n) ")
                            if "y" in x.lower():
                                x = input("Are you sure as never been before? (y/n) ")
                                if "y" in x.lower():
                                    x = input("Are you really sure as never been before? (y/n) ")
                                    if "y" in x.lower():
                                        x = input("Are you really really sure as never been before? (y/n) ")
                                        if "y" in x.lower():
                                            x = input("Are you sure as really never been before? (y/n) ")
                                            if "y" in x.lower():
                                                x = input("Are you really sure as really never been before? (y/n) ")
                                                if "y" in x.lower():
                                                    x = input("Are you really really sure as really never been before? (y/n) ")
                                                    if "y" in x.lower():
                                                        x = input("Are you sure as really really never been before? (y/n) ")
                                                        if "y" in x.lower():
                                                            x = input("Are you really sure as really really never been before? (y/n) ")
                                                            if "y" in x.lower():
                                                                x = input("Are you really really sure as really really never been before? (y/n) ")
                                                                if "y" in x.lower():
                                                                    x = input("Are you actually sure? (y/n) ")
                                                                    if "y" in x.lower():
                                                                        x = input("This is my last warning. (y/n) ")
                                                                        if "y" in x.lower():
                                                                            x = input("Ask everyone. (y/n) ")
                                                                            if "y" in x.lower():
                                                                                x = input("Ask everyone that's using this chat. (y/n) ")
                                                                                if "y" in x.lower():
                                                                                    x = input("Ask literally everyone that's using this chat. (y/n) ")
                                                                                    if "y" in x.lower():
                                                                                        x = input("Ask literally everyone that's using this chat for real. (y/n) ")
                                                                                        if "y" in x.lower():
                                                                                            x = input("Ask your mother. (y/n) ")
                                                                                            if "y" in x.lower():
                                                                                                x = input("Ask your father. (y/n) ")
                                                                                                if "y" in x.lower():
                                                                                                    x = input("Ask your grandmother. (y/n) ")
                                                                                                    if "y" in x.lower():
                                                                                                        x = input("Ask your wife's boyfriend. (y/n) ")
                                                                                                        if "y" in x.lower():
                                                                                                            x = input("There's no turning back. (y/n) ")
                                                                                                            if "y" in x.lower():
                                                                                                                x = input("Okay. (y/n) ")
                                                                                                                if "y" in x.lower():
                                                                                                                    f = open("chat.txt", "w")
                                                                                                                    f.write("")
                                                                                                                    f.close()
                                                                                                                    print("Chat deleted.")
            elif x == 7:
                print("Welcome to FOS Sub-OS!")
                while True:
                    x = input("Exit FOS Sub-OS? (y/n) ")
                    if "y" in x.lower():
                        break
                    print("List of apps:")
                    print('"1" for word-number edit module')
                    print('"2" for minecraft (the video game one)')
                    print('"3" for 200000-slot memory')
                    print('"4" for random module basics')
                    print('"5" for a text-based adventure game made by ChatGPT')
                    print('"6" for calory tracker assistant')
                    print('"7" for a small grid game')
                    x = int(input("What to open?  "))
                    if x == 1:
                        print('"1" for addition')
                        print('"2" for subtraction')
                        print('"3" for multiplication')
                        print('"4" for division')
                        print('"5" for modulus')
                        print('"6" for exponentiation')
                        print('"7" for floor division')
                        print('"8" for floor')
                        print('"9" for ceiling')
                        print('"10" for rounding')
                        print('"11" for capitalization')
                        print('"12" for uppercase')
                        print('"13" for lowercase')
                        print('"14" for case swap')
                        print('"15" for equal')
                        print('"16" for not equal')
                        print('"17" for greater than')
                        print('"18" for lesser than')
                        print('"19" for greater than or equal')
                        n = int(input('"20" for lesser than or equal    '))
                        if n == 1:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x + y)
                        if n == 2:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x - y)
                        if n == 3:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x * y)
                        if n == 4:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x / y)
                        if n == 5:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x % y)
                        if n == 6:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x ** y)
                        if n == 7:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print(x // y)
                        if n == 8:
                            x = float(input("Insert number "))
                            print(x - (x % 1))
                        if n == 9:
                            x = float(input("Insert number "))
                            print((x - (x % 1)) + 1)
                        if n == 10:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 (to the nearest n number) "))
                            print(float(int(x / y) * y))
                        if n == 11:
                            x = input("Insert word ")
                            print(x.capitalize())
                        if n == 12:
                            x = input("Insert word ")
                            print(x.upper())
                        if n == 13:
                            x = input("Insert word ")
                            print(x.lower())
                        if n == 14:
                            x = input("Insert word ")
                            print(x.swapcase())
                        if n == 15:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x == y:
                                print("x = y")
                            else:
                                print("x ≠ y")
                        if n == 16:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x == y:
                                print("x = y")
                            else:
                                print("x ≠ y")
                        if n == 17:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x > y:
                                print("x > y")
                            else:
                                print("x < y")
                        if n == 18:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x < y:
                                print("x < y")
                            else:
                                print("x > y")
                        if n == 19:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x >= y:
                                print("x >= y")
                            else:
                                print("x !>= y")
                        if n == 20:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            if x <= y:
                                print("x <= y")
                            else:
                                print("x !<= y")
                    if x == 2:
                        print("MINECRAFT")
                        print("Text-based python port")
                        print("There's 30 features.")
                        print("20 for Crafting,")
                        print("5 for Adventures.")
                        print("You can lose but can't win.")
                        print("Made with more than 100 lines of code")
                        print("Luck-based game.")
                        input("Answer to start. ")
                        pata = 0
                        sword = 0
                        pickaxe = 0
                        shovel = 0
                        axe = 0
                        hoe = 0
                        game = "play"
                        while game == "play":
                            if randint(1, 2) == 1:
                                if randint(1, 5) == 1:
                                    print("You've found wood!")
                                    chop = 1
                                else:
                                    if randint(1, 4) == 1:
                                        print("You've found stone!")
                                        chop = 2
                                    else:
                                        if randint(1, 3) == 1:
                                            print("You've found iron!")
                                            chop = 3
                                        else:
                                            if randint(1, 2) == 1:
                                                print("You've found diamonds!")
                                                chop = 4
                                            else:
                                                print("You've found netherite!")
                                                chop = 5
                                print("What to craft?")
                                print("Options:")
                                print("Sword")
                                print("Pickaxe")
                                print("Axe")
                                print("Shovel")
                                print("Hoe")
                                tool = input("Please write your answer lowercase. ")
                                if tool == "sword":
                                    sword = sword + chop
                                if tool == "pickaxe":
                                    pickaxe = pickaxe + chop
                                if tool == "axe":
                                    axe = axe + chop
                                if tool == "shovel":
                                    shovel = shovel + chop
                                if tool == "hoe":
                                    hoe = hoe + chop
                            else:
                                if randint(1, 5) == 5:
                                    decision = input("Mobs have come! Use a sword? (y/n) ")
                                    if decision == "y":
                                        sword = sword - 1
                                    else:
                                        game = "stop"
                                else:
                                    if randint(1, 4) == 4:
                                        decision = input("You found an ore! Use pickaxe? (y/n) ")
                                        if decision == "y":
                                            pickaxe = pickaxe - 1
                                        else:
                                            game = "stop"
                                    else:
                                        if randint(1, 3) == 3:
                                            decision = input("You'll chop trees! Use an axe? (y/n) ")
                                            if decision == "y":
                                                axe = axe - 1
                                            else:
                                                game = "stop"
                                        else:
                                            if randint(1, 2) == 2:
                                                decision = input("You'll dig a hill! Use a shovel? (y/n) ")
                                                if decision == "y":
                                                    shovel = shovel - 1  # longest indent
                                                else:
                                                    game = "stop"
                                            else:
                                                decision = input("You made a farm! Use a hoe? (y/n) ")
                                                if decision == "y":
                                                    hoe = hoe - 1
                                                else:
                                                    game = "stop"
                            inventory = input("Show inventory? (y/n) ")
                            if inventory == "y" and game == "play":
                                if sword > 0:
                                    print("Swords:")
                                    print(sword)
                                if pickaxe > 0:
                                    print("Pickaxes:")
                                    print(pickaxe)
                                if axe > 0:
                                    print("Axes:")
                                    print(axe)
                                if shovel > 0:
                                    print("Shovels:")
                                    print(shovel)
                                if hoe > 0:
                                    print("Hoes:")
                                    print(hoe)
                            if sword < 0:
                                game = "stop"
                            if pickaxe < 0:
                                game = "stop"
                            if axe < 0:
                                game = "stop"
                            if shovel < 0:
                                game = "stop"
                            if hoe < 0:
                                game = "stop"
                            pata = pata + 1
                        print("YOU LOSE!")
                        print("Score:")
                        print(pata)
                    if x == 3:
                        print("1 to change something in the 200000 slot-memory")
                        n = int(input("2 to find data in the 200000 slot-memory "))
                        if n == 1:
                            x = int(input("Write the slot you want to change in the 200000 slots. "))
                            y = input("Write the new thing you want it to change. ")
                            fruits[x] = y
                        if n == 2:
                            x = int(
                                input("Write the slot you want to learn what's inside in the 200000 slots. "))
                            print(fruits[x])
                    if x == 4:
                        print("1 to find a full random number")
                        print("2 to find a random decimal number from the distribution")
                        n = int(input("3 to find a random decimal number "))
                        if n == 1:
                            x = int(input("Insert number 1 "))
                            y = int(input("Insert number 2 "))
                            print(randint(x, y))
                        if n == 2:
                            x = float(input("Insert average (mu) "))
                            y = float(input("Insert standard deviation (sigma) "))
                            print(gauss(x, y))
                        if n == 3:
                            x = float(input("Insert number 1 "))
                            y = float(input("Insert number 2 "))
                            print((random() * (y + x)) - x)
                    if x == 5:
                        grid_size = 5
                        grid = [['Empty' for _ in range(grid_size)] for _ in range(grid_size)]
                        player_position = [0, 0]
                        inventory = []

                        events = ['Found an item', 'Encountered an enemy', 'Nothing happened']
                        for i in range(grid_size):
                            for j in range(grid_size):
                                grid[i][j] = choice(events)


                        def display_grid():
                            for row in grid:
                                print(' | '.join(row))
                            print()


                        def display_position():
                            print(f'Player position: {player_position}')
                            print(f'Current cell: {grid[player_position[0]][player_position[1]]}')
                            print()


                        def display_inventory():
                            print(f'Inventory: {inventory}')
                            print()


                        def move_player(direction):
                            if direction == 'up' and player_position[0] > 0:
                                player_position[0] -= 1
                            elif direction == 'down' and player_position[0] < grid_size - 1:
                                player_position[0] += 1
                            elif direction == 'left' and player_position[1] > 0:
                                player_position[1] -= 1
                            elif direction == 'right' and player_position[1] < grid_size - 1:
                                player_position[1] += 1
                            else:
                                print("Can't move in that direction!")
                            event = grid[player_position[0]][player_position[1]]
                            handle_event(event)


                        def handle_event(event):
                            if event == 'Found an item':
                                item = choice(['Sword', 'Shield', 'Potion'])
                                inventory.append(item)
                                print(f'You found a {item}!')
                            elif event == 'Encountered an enemy':
                                print('You encountered an enemy! Prepare to fight!')
                            elif event == 'Nothing happened':
                                print('Nothing happened here.')
                            grid[player_position[0]][player_position[1]] = 'Visited'


                        def game_loop():
                            while True:
                                display_grid()
                                display_position()
                                display_inventory()
                                move = input("Move (up/down/left/right) or 'quit' to exit: ").strip().lower()
                                if move in ['up', 'down', 'left', 'right']:
                                    move_player(move)
                                elif move == 'quit':
                                    print("Thanks for playing!")
                                    break
                                else:
                                    print("Invalid input, please try again.")


                        if __name__ == "__main__":
                            print("Welcome to the Text-Based Adventure Game!")
                            game_loop()
                    if x == 6:
                        print("Hello!")
                        print("I'm your diet assistant!")
                        print("I will make a plan so you will get warned when you eat too much.")
                        x = input("First enter gender. M/F/N (Male, female, neutral [any gender])    ")
                        if x.upper() == "M":
                            kcal = 2500
                        elif x.upper() == "F":
                            kcal = 2000
                        else:
                            kcal = 2250
                        print(kcal, " kcal until the limit for today!")
                        print("When you plan to eat something, just tell me by writing a number.")
                        print("1 - almond")
                        print("2 - apple")
                        print("3 - bagel")
                        print("4 - banana")
                        print("5 - beer")
                        print("6 - big mac")
                        print("7 - bread")
                        print("8 - cake")
                        print("9 - carrot")
                        print("10 - chicken nugget")
                        print("11 - chips")
                        print("12 - coke")
                        print("13 - donut")
                        print("14 - egg")
                        print("15 - m&m")
                        print("16 - peanut butter cup")
                        print("17 - pizza")
                        print("18 - rice")
                        print("19 - sushi")
                        print("20 - whopper")
                        list = [2500 / 325, 2500 / 16, 2500 / 7, 2500 / 19, 2500 / 28, 2500 / 4, 2500 / 13,
                                2500 / 4,
                                2500 / 65, 2500 / 37, 2500 / 4, 2500 / 14, 2500 / 7, 2500 / 26, 2500 / 400,
                                2500 / 18,
                                2500 / 7, 2500 / 8, 2500 / 48, 2500 / 3]
                        credit = input('Write "y" if you want to see the acknowledgements. ')
                        if credit.lower() == "y":
                            print(
                                'Thanks for the YouTube user "Sambucha" for his video "https://www.youtube.com/shorts/NeN-0AbV3z0" for the kcal information.')
                        game = "play"
                        while game == "play":
                            for i in range(20):
                                pref = input(
                                    'Please write the corresponding number of what you\'ve eaten. (Write "0" if you ate nothing.) Write "esc" if you want to quit. ')
                                if pref.lower() == "esc":
                                    print(
                                        "Before you quit, please let me say that my only duty is to track how many calories you get daily.")
                                    game = "stop"
                                elif not (pref == 0):
                                    kcal = kcal - list[int(pref) - 1]
                                    if kcal <= 0:
                                        print("You've eaten too much!")
                                        print("To punish you, here is an irony :)")
                                        print(your_diet)
                                print(kcal, " kcal until the limit for today!")
                            print("When you plan to eat something, just tell me by writing a number.")
                            print("1 - almond")
                            print("2 - apple")
                            print("3 - bagel")
                            print("4 - banana")
                            print("5 - beer")
                            print("6 - hamburger")
                            print("7 - bread")
                            print("8 - cake")
                            print("9 - carrot")
                            print("10 - chicken nugget")
                            print("11 - chips")
                            print("12 - coke")
                            print("13 - donut")
                            print("14 - egg")
                            print("15 - sweets")
                            print("16 - peanut butter cup")
                            print("17 - pizza")
                            print("18 - rice")
                            print("19 - sushi")
                            print("20 - bacon burger")
                            list = [2500 / 325, 2500 / 16, 2500 / 7, 2500 / 19, 2500 / 28, 2500 / 4, 2500 / 13,
                                    2500 / 4, 2500 / 65, 2500 / 37, 2500 / 4, 2500 / 14, 2500 / 7, 2500 / 26,
                                    2500 / 400, 2500 / 18, 2500 / 7, 2500 / 8, 2500 / 48, 2500 / 3]
                    if x == 7:
                        grid = []
                        for i in range(100):
                            grid.append("▧")
                        print(
                            'HOW TO PLAY: This game is a game where there is a 10x10 grid and you spawn on coordinates 1, 1. You can do some commands. They are left, right, up, down, quit, howtoplay, and "symbols". When you write a symbol, the game puts that symbol to your current position. Here are some default symbols to use: ▣◩◪▧◰□♠♣♥♦🌲🌳🌴🪵🪨💎🧱🪙🍄🔑 ')


                        def coordinate():
                            map = 0
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 10
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 20
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 30
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 40
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 50
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 60
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 70
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 80
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])
                            map = 90
                            print(grid[map], grid[map + 1], grid[map + 2], grid[map + 3], grid[map + 4],
                                  grid[map + 5],
                                  grid[map + 6], grid[map + 7], grid[map + 8], grid[map + 9])


                        t = input(
                            "1 for matrix notation co-ordinate system (y, x)\n2 for mapping notation co-ordinate system (x, y) ")
                        game = "play"
                        lat = 1
                        long = 1
                        while game == "play":
                            coordinate()
                            if t == "1":
                                print("Position: ", long, ", ", lat)
                            elif t == "2":
                                print("Position: ", lat, ", ", long)
                            else:
                                print("INVALID CO-ORDINATES!")
                                game = "stop"
                            gr = input("What command do you want? ")
                            if gr.lower() == "left":
                                if lat != 1:
                                    lat = lat - 1
                            elif gr.lower() == "right":
                                if lat != 10:
                                    lat = lat + 1
                            elif gr.lower() == "up":
                                if long != 1:
                                    long = long - 1
                            elif gr.lower() == "down":
                                if long != 10:
                                    long = long + 1
                            elif gr.lower() == "quit":
                                game = "stop"
                            elif gr.lower() == "howtoplay":
                                print('HOW TO PLAY: This game is a game where there is a 10x10 grid and you spawn on coordinates 1, 1. You can do some commands. They are left, right, up, down, quit, howtoplay, and "symbols". When you write a symbol, the game puts that symbol to your current position. Here are some default symbols to use: ▣◩◪▧◰□♠♣♥♦🌲🌳🌴🪵🪨💎🧱🪙🍄🔑')
                            elif len(gr) == 1:
                                grid[(long - 1) * 10 + lat - 1] = gr
            elif x == 8:
                print("1 to open budget manager")
                print("2 to open logic evaluator")
                print("3 to open CASINO MINIGAMES")
                print("4 to open Yacht Dice (Yahtzee)")
                print("5 to open utilities")
                x = int(input("\n"))
                if x == 1:
                    print("Welcome to budget manager!")
                    print("Here, you can manage your budget.")
                    print("Using 3 currencies: Knut, Sickle, Galleon")
                    x = input("First, do you want to record your budget to a file (y/n)? ")
                    if "y" in x.lower():
                        x = input("File name: ")
                        y = input(f"Delete old text in {x} (y/n)? ")
                        if "y" in x.lower():
                            f = open(x, "w")
                            f.write("Budget Manager Data")
                            f.close()
                        f = open(x, "a")
                        file = True
                    budget = 0
                    user = input("Username: ")
                    if file:
                        f.write(f"Budget of {user}\n")
                    while True:
                        if file:
                            f.write(f"Knuts (Bronze): {budget}\n")
                            f.write(f"Sickles (Silver): {budget * 29}\n")
                            f.write(f"Galleons (Gold): {budget * 493}\n")
                        print("1 to print money")
                        print("2 to change money")
                        print("3 to quit")
                        x = int(input("\n"))
                        if x == 1:
                            print(f"Knuts (Bronze): {budget}\n")
                            print(f"Sickles (Silver): {budget * 29}\n")
                            print(f"Galleons (Gold): {budget * 493}\n")
                        elif x == 2:
                            print("1 to add money")
                            print("2 to subtract money")
                            x = int(input("\n"))
                            if x == 1:
                                print("1 to add Knuts")
                                print("2 to add Sickles")
                                print("3 to add Galleons")
                                x = int(input("\n"))
                                if x == 1:
                                    x = int(input("Add how many Knuts? "))
                                    if file:
                                        f.write(f"Added {x} Knuts\n")
                                    budget += x
                                elif x == 2:
                                    x = int(input("Add how many Sickles? "))
                                    if file:
                                        f.write(f"Added {x} Sickles\n")
                                    budget += x * 29
                                elif x == 3:
                                    x = int(input("Add how many Galleons? "))
                                    if file:
                                        f.write(f"Added {x} Galleons\n")
                                    budget += x * 493
                            elif x == 2:
                                print("1 to subtract Knuts")
                                print("2 to subtract Sickles")
                                print("3 to subtract Galleons")
                                x = int(input("\n"))
                                if x == 1:
                                    x = float(input("Subtract how many Knuts? "))
                                    if file:
                                        f.write(f"Subtracted {x} Knuts\n")
                                    budget -= x
                                elif x == 2:
                                    x = float(input("Subtract how many Sickles? "))
                                    if file:
                                        f.write(f"Subtracted {x} Sickles\n")
                                    budget -= x * 29
                                elif x == 3:
                                    x = float(input("Subtract how many Galleons? "))
                                    if file:
                                        f.write(f"Subtracted {x} Galleons\n")
                                    budget -= x * 493
                        elif x == 3:
                            break
                elif x == 2:
                    print("1 to evaluate Python logic")
                    print("2 to evaluate Boolean logic")
                    print("3 to evaluate decimal logic")
                    print("4 to evaluate binary logic")
                    print("5 to evaluate Batch logic")
                    print("6 to open logic gate simulator")
                    x = int(input("\n"))
                    if x == 1:
                        print("Enter a Python data and it'll give the answer.")
                        print("E.g. write \"5 + 5\" and the program will print \"10\".")
                        x = input("Enter data: ")
                        print(eval(x))
                    elif x == 2:
                        print("Enter a Python data and it'll give the Bool value.")
                        print("E.g. write \"5+5 == 10\" and the program will print \"True\".")
                        x = input("Enter data: ")
                        if type(eval(x)) == bool:
                            print(eval(x))
                        else:
                            print("Unknown")
                    elif x == 3:
                        print("Enter a Python decimal operation and it'll give the answer.")
                        print("E.g. write \"5 + 5\" and the program will print \"10\".")
                        x = input("Enter data: ")
                        print(float(eval(x)))
                    elif x == 4:
                        print("Enter a Python decimal operation and it'll give the binary value.")
                        print("E.g. write \"5 + 5\" and the program will print \"1010\".")
                        x = int(input("Enter data: "))
                        print(bin(x)[2:])
                    elif x == 5:
                        print("Enter a Batch data and it'll give the answer.")
                        print("E.g. write \"$((5 + 5))\" and the program will print \"10\".")
                        x = input("Enter data: ")
                        system(f"echo {x}")
                    elif x == 6:
                        print("Welcome to the Logic Gate Simulator!")
                        print("First, select the number of buttons:")
                        print("1 to use 1 buttons")
                        print("2 to use 2 buttons")
                        print("3 to open logic gate cheatsheet")
                        x = int(input("\n"))
                        if x == 1:
                            print("1 button connects to 1 lightbulb.")
                            print("Both can be True and False.")
                            print("Enter the logic gate between button 1 and bulb to gate 1 from: WIRE, BUFFER, NOT, RAND to gate 1")
                            print("Enter the button's bool value to button 1.")
                            g1 = input("Gate 1: ")
                            b1 = bool(input("Button 1: "))
                            g1 = g1.lower()
                            if g1 == "wire" or g1 == "buffer":
                                pass
                            elif g1 == "not":
                                b1 = not(b1)
                            elif g4 == "rand":
                                b1 = choice(tf)
                            print(f"Bulb is {b1}")
                        elif x == 2:
                            print("2 buttons connects to 1 lightbulb.")
                            print("Both can be True and False.")
                            print("Enter the logic gate between button 1 and bulb to gate 3 from: WIRE, BUFFER, NOT, RAND to gate 1")
                            print("Enter the logic gate between button 2 and bulb to gate 3 from: WIRE, BUFFER, NOT, RAND to gate 2")
                            print("Enter the logic gate on button 1 and 2's wires' connection point from: OR, XOR, NOR, XNOR, NXOR, AND, XAND, NAND, XNAND, NXAND, IMPLY, XIMPLY, NIMPLY, XNIMPLY, NXIMPLY, RAND to gate 3")
                            print("Enter the logic gate between gate 3 to bulb from: WIRE, BUFFER, NOT, RAND to gate 4")
                            print("Enter the button's bool value to button 1.")
                            g1 = input("Gate 1: ")
                            g2 = input("Gate 2: ")
                            g3 = input("Gate 3: ")
                            g4 = input("Gate 4: ")
                            b1 = bool(input("Button 1: "))
                            b2 = bool(input("Button 2: "))
                            g1 = g1.lower()
                            g2 = g2.lower()
                            g3 = g3.lower()
                            g4 = g4.lower()
                            if g1 == "wire" or g1 == "buffer":
                                pass
                            elif g1 == "not":
                                b1 = not(b1)
                            elif g4 == "rand":
                                b1 = choice(tf)
                            if g2 == "wire" or g2 == "buffer":
                                pass
                            elif g2 == "not":
                                b2 = not(b2)
                            elif g4 == "rand":
                                b1 = choice(tf)
                            if g3 == "or":
                                b1 = b1 or b2
                            elif g3 == "xor" or g3 == "xnand" or g3 == "nxand" or g3 == "norxondorgorgonax":
                                if (b1 or b2) and (b1 and b2):
                                    b1 = False
                                else:
                                    b1 = b1 or b2
                            elif g3 == "nor":
                                b1 = not(b1 or b2)
                            elif g3 == "xnor" or g3 == "nxor" or g3 == "xand":
                                if (b1 or b2) and (b1 and b2):
                                    b1 = True
                                else:
                                    b1 = not(b1 or b2)
                            elif g3 == "nand":
                                b1 = not(b1 and b2)
                            elif g3 == "imply":
                                if b1 and not(b2):
                                    b1 = False
                                else:
                                    b1 = True
                            elif g3 == "ximply":
                                if b1 and not(b2):
                                    b1 = False
                                elif b1 and b2:
                                    b1 = False
                                else:
                                    b1 = True
                            elif g3 == "nimply":
                                if b1 and not(b2):
                                    b1 = True
                                else:
                                    b1 = False
                            elif g3 == "xnimply" or g3 == "nximply":
                                if b1 and not(b2):
                                    b1 = False
                                elif b1 and b2:
                                    b1 = False
                                else:
                                    b1 = True
                            elif g3 == "rand":
                                b1 = choice(tf)
                            if g4 == "wire" or g4 == "buffer":
                                pass
                            elif g4 == "not":
                                b1 = not(b1)
                            elif g4 == "rand":
                                b1 = choice(tf)
                            print(f"Bulb is {b1}")
                        elif x == 3:
                            print("Singular Button Logic Gates")
                            print("WIRE - 0 = 0, 1 = 1")
                            print("BUFFER - 0 = 0, 1 = 1")
                            print("NOT - 0 = 1, 1 = 0")
                            print("RAND - 0, 1 = random.choice([True, False])")
                            print("Plural Button Logic Gates")
                            print("OR - 00 = 0, 10 = 1, 01 = 1, 11 = 1")
                            print("XOR - 00 = 0, 10 = 1, 01 = 1, 11 = 0")
                            print("NOR - 00 = 1, 10 = 0, 01 = 0, 11 = 0")
                            print("XNOR - 00 = 1, 10 = 0, 01 = 0, 11 = 1")
                            print("NXOR - 00 = 1, 10 = 0, 01 = 0, 11 = 1")
                            print("XNOR - 00 = 1, 10 = 0, 01 = 0, 11 = 1")
                            print("AND - 00 = 0, 10 = 0, 01 = 0, 11 = 1")
                            print("XAND - 00 = 1, 10 = 0, 01 = 0, 11 = 1")
                            print("NAND - 00 = 1, 10 = 1, 01 = 1, 11 = 0")
                            print("XNAND - 00 = 0, 10 = 1, 01 = 1, 11 = 0")
                            print("NXAND - 00 = 0, 10 = 1, 01 = 1, 11 = 0")
                            print("IMPLY - 00 = 1, 10 = 0, 01 = 1, 11 = 1")
                            print("XIMPLY - 00 = 1, 10 = 0, 01 = 1, 11 = 0")
                            print("NIMPLY - 00 = 0, 10 = 1, 01 = 0, 11 = 0")
                            print("XNIMPLY - 00 = 0, 10 = 1, 01 = 0, 11 = 1")
                            print("XNIMPLY - 00 = 0, 10 = 1, 01 = 0, 11 = 1")
                            print("RAND - 00, 10, 01, 11= random.choice([True, False])")
                elif x == 3:
                    print("1 to open lottery")
                    print("2 to open ROULETTE")
                    print("3 to open slots")
                    x = int(input("\n"))
                    if x == 1:
                        print("Welcome to the roulette!")
                        while True:
                            print("1 to open rules")
                            print("4 to play")
                            x = int(input("\n"))
                            if x == 1:
                                print("In lottery, you get a ticket and it has numbers.\nIn the television, the winning numbers get announced.")
                                print("You get money according to your numbers.\nYou can simulate winning numbers and how much money you win.")
                            elif x == 2:
                                money = float(input("Enter your budget: "))
                                moneyold = money
                                money -= bet
                                print(f"Budget: ${money}")
                                print("1 to simulate winning numbers")
                                print("2 to simulate money")
                                print("3 or else to quit")
                                x = int(input("\n"))
                                if x == 1:
                                    print(f"Your ticket's numbers: {randint(0, 99)} {randint(0, 99)} {randint(0, 99)} {randint(0, 99)} {randint(0, 99)}")
                                    print(f"Winning numbers:       {randint(0, 99)} {randint(0, 99)} {randint(0, 99)} {randint(0, 99)} {randint(0, 99)}")
                                elif x == 2:
                                    print("Ticket bought for $10.")
                                    money -= 10
                                    list1 = [1]
                                    list2 = [1, 2]
                                    list3 = [1, 2, 3, 4]
                                    list4 = [1, 2, 3, 4, 5, 6, 7, 8]
                                    if randint(1, 100) in list1:
                                        x = 200
                                    elif randint(1, 100 - 1) in list2:
                                        x = 100
                                    elif randint(1, 100 - 1 - 2) in list3:
                                        x = 50
                                    elif randint(1, 100 - 1 - 2 - 4) in list4:
                                        x = 10
                                    else:
                                        x = 0
                                    print(f"You won ${x} from the ticket.")
                                    money += x
                                else:
                                    break
                        if money < 0:
                            print(
                                "You've exited the casino. While gambling, your budget has gone negative, but you kept gambling.")
                            print("You got beaten up by the casino members. You don't feel well.")
                            print("You lost. Ending #5: Bankruptcy")
                            print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                        if money == 0:
                            print("You've exited the casino. While gambling, you've lost all your money.")
                            print("You are now poor. Good luck giving even the smallest tax.")
                            print("You lost. Ending #4: Bankruptcy")
                            print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                        if money < moneyold:
                            print("You've exited the casino. While gambling, you've lost some money.")
                            print(
                                "You are now poorer than start. Quit gambling please, but at least, you can live fine.")
                            print("You lost. Ending #3: Poor")
                            print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                        if money == moneyold:
                            print("You've exited the casino. While gambling, your money stayed the same.")
                            print(
                                "Nothing changed. I don't know if this is a win or loss, but at least you didn't lose money.")
                            print("You won. Ending #2: Nothing")
                            print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                        if money > moneyold:
                            print("You've exited the casino. While gambling, you've won some money.")
                            print(
                                "You are now rich a bit. Will you continue? Know that winning by gambling is stealing, effort exploiting and a sin.")
                            print("You lost. Ending #1: Rich (the Sinner's Way)")
                            print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                    elif x == 2:
                        print("1 to play European roulette")
                        print("2 to play RUSSIAN ROULETTE")
                        x = int(input("\n"))
                        if x == 1:
                            print("Welcome to the roulette!")
                            while True:
                                print("1 to open rules")
                                print("2 to get tactics")
                                print("3 to get number betting and prize cheastsheet")
                                print("4 to play")
                                x = int(input("\n"))
                                if x == 1:
                                    print("In roulette, you bet an amount of numbers,\nand win money if the numbers were selected in a random number selection.")
                                    print("There's 37 numbers from 0 to 36.\nTo increase your chances to win, look at some tactics!")
                                elif x == 2:
                                    print("Martingale: If you lose, double the bet's number.")
                                    print("Fibonacci: Bet the Fibonacci number sequence in order.")
                                    print("D'Alembert: Bet 1 number higher if lost, and 1 number lower if won.")
                                elif x == 3:
                                    print("Options of numbers to bet for: Prize:")
                                    print("1 (Straight Up)                36 times how much got bet to roulette")
                                    print("2 (Split)                      18 times how much got bet to roulette")
                                    print("3 (Street)                     12 times how much got bet to roulette")
                                    print("4 (Corner)                     9 times how much got bet to roulette")
                                    print("6 (Six Line)                   6 times how much got bet to roulette")
                                    print("12 (Dozen)                     3 times how much got bet to roulette")
                                    print("18 (Even Money Bet)            2 times how much got bet to roulette")
                                elif x == 4:
                                    money = float(input("Enter your budget: "))
                                    moneyold = money
                                    bet = float(input("Bet how much money for the roulette? "))
                                    money -= bet
                                    print(f"Budget: ${money}")
                                    print("1 to play")
                                    print("2 or else to quit")
                                    x = int(input("\n"))
                                    if x == 1:
                                        print("1 to bet straight up")
                                        print("2 to bet split")
                                        print("3 to bet street")
                                        print("4 to bet corner")
                                        print("5 to bet six lane")
                                        print("6 to bet dozen")
                                        print("7 to bet even money bet")
                                        x = int(input("\n"))
                                        input("Bet which numbers? ")
                                        if x == 1:
                                            if randint(1, 37) <= 1:
                                                print(f"You won!\n${bet * 36} added")
                                                budget += bet * 36
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 2:
                                            if randint(1, 37) <= 2:
                                                print(f"You won!\n${bet * 18} added")
                                                budget += bet * 2
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 3:
                                            if randint(1, 37) <= 3:
                                                print(f"You won!\n${bet * 12} added")
                                                budget += bet * 12
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 4:
                                            if randint(1, 37) <= 4:
                                                print(f"You won!\n${bet * 9} added")
                                                budget += bet * 9
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 5:
                                            if randint(1, 37) <= 6:
                                                print(f"You won!\n${bet * 6} added")
                                                budget += bet * 6
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 5:
                                            if randint(1, 37) <= 12:
                                                print(f"You won!\n${bet * 3} added")
                                                budget += bet * 3
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                        elif x == 1:
                                            if randint(1, 37) <= 18:
                                                print(f"You won!\n${bet * 2} added")
                                                budget += bet * 2
                                                print(f"Budget: ${money}")
                                            else:
                                                print("You lost!")
                                                print(f"Budget: ${money}")
                                    else:
                                        break
                            if money < 0:
                                print("You've exited the casino. While gambling, your budget has gone negative, but you kept gambling.")
                                print("You got beaten up by the casino members. You don't feel well.")
                                print("You lost. Ending #5: Bankruptcy")
                                print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                            if money == 0:
                                print("You've exited the casino. While gambling, you've lost all your money.")
                                print("You are now poor. Good luck giving even the smallest tax.")
                                print("You lost. Ending #4: Bankruptcy")
                                print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                            if money < moneyold:
                                print("You've exited the casino. While gambling, you've lost some money.")
                                print("You are now poorer than start. Quit gambling please, but at least, you can live fine.")
                                print("You lost. Ending #3: Poor")
                                print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                            if money == moneyold:
                                print("You've exited the casino. While gambling, your money stayed the same.")
                                print("Nothing changed. I don't know if this is a win or loss, but at least you didn't lose money.")
                                print("You won. Ending #2: Nothing")
                                print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                            if money > moneyold:
                                print("You've exited the casino. While gambling, you've won some money.")
                                print("You are now rich a bit. Will you continue? Know that winning by gambling is stealing, effort exploiting and a sin.")
                                print("You lost. Ending #1: Rich (the Sinner's Way)")
                                print(f"Budget in the start: ${moneyold} Budget now: ${money}")
                        elif x == 2:
                            print("Welcome to the RUSSIAN ROULETTE!")
                            while True:
                                print("1 to open rules")
                                print("2 to PLAY")
                                x = int(input("\n"))
                                if x == 1:
                                    print("In RUSSIAN roulette, someone inserts a bullet to a gun.\nThen, he spins the bullet wheel, now we don't know at which shot the bullet will ignite.")
                                    print("Everyone shots the gun at himself in order.\nThere are 6 places the bullet could be placed. The bullet could ignite in tour 1 to 6.")
                                    print("The thing is anyone playing has the chance to die.")
                                elif x == 2:
                                    print("1 to PLAY")
                                    print("2 or else to quit")
                                    x = int(input("\n"))
                                    if x == 1:
                                        names = ['Alexander', 'Alexei', 'Anatolyevich', 'Andrei', 'Andreyevich',
                                                 'Boris', 'Borisovich', 'Dmitriy', 'Dmitry', 'Fyodorovich', 'Georgy',
                                                 'Grigoriy', 'Igor', 'Ilyich', 'Joseph', 'Konstantin', 'Lavrentiy',
                                                 'Leonid', 'Lev', 'Maximilianovich', 'Mikhail', 'Mikhaylovich',
                                                 'Nikita', 'Nikolai', 'Nikolayevich', 'Pavlovich', 'Sergeyevich',
                                                 'Stepanovich', 'Ustinovich', 'Viassarionovich', 'Viktor',
                                                 'Viktorovich', 'Vladimir', 'Vladimirovich', 'Vyacheslav',
                                                 'Yevseyevich', 'Yuri']
                                        shuffle(names)
                                        list = []
                                        username = input("Your name: ")
                                        for i in range(randint(1, 6)):
                                            list.append(names.pop())
                                        list.append(username)
                                        shuffle(list)
                                        x = randint(1, 5)
                                        print(f"Players: {list}")
                                        for i in range(x):
                                            print(f"Round {i + 1}/6")
                                            print(f"{list[i]} will now shoot")
                                            print("The bullet didn't ignited!")
                                        print(f"Round {x + 1}/6")
                                        print(f"{list[x]} will now shoot")
                                        print("The bullet ignited!")
                                        print("", end = "")
                                    else:
                                        break
                        elif x == 3:
                            while True:
                                print("1 to open rules")
                                print("2 to play")
                                x = int(input("\n"))
                                if x == 1:
                                    print("In slots, you pull a lever. 3 slots will spin.\nIf the slots match, you win.")
                                elif x == 2:
                                    print("1 to play")
                                    print("2 or else to quit")
                                    x = int(input("\n"))
                                    if x == 1:
                                        print("Lever pulling...")
                                        list = ""
                                        for i in range(3):
                                            list = f"{list}{food[randint(0, 4)]}"
                                        print(f"Slot results: {list}")
                                        if list[0] == list[1] and list[1] == list[2]:
                                            print("You won!")
                                        else:
                                            print("You lose!")
                elif x == 4:
                    while True:
                        del list
                        print("1 to open rules")
                        print("2 to see cheatsheet")
                        print("3 to play")
                        if x == 1:
                            print("In Yacht Dice, you roll 5 dices.\nYou can keep and reroll dices up to 3 tours.")
                            print("Then, you select a point type where you get points according to your dices.")
                            print("You (and opponent) will play 12 tours, and get points.\nThe player with the most points win.")
                            print("Look at the cheatsheet to see the point types.")
                        elif x == 2:
                            print("UPPER SECTION")
                            print("Aces-Sum of all 1's")
                            print("Deuces-Sum of all 2's")
                            print("Threes-Sum of all 3's")
                            print("Fours-Sum of all 4's")
                            print("Fives-Sum of all 5's")
                            print("Sixes-Sum of all 6's")
                            print("LOWER SECTION")
                            print("3 of a kind-Total of all dices if there's 3 of same number")
                            print("4 of a kind-Total of all dices if there's 4 of same number")
                            print("Full house-50 if there's 3, and 2 of a kind")
                            print("Yahtzee-25 if there's 5 of same number")
                            print("Small straight-30 if sequence of 4")
                            print("Large straight-40 if sequence of 5")
                            print("Chance-Sum of all dice")
                        elif x == 3:
                            print("1 to play")
                            print("2 or else to quit")
                            x = int(input("\n"))
                            if x == 1:
                                p1 = 0
                                p2 = 0
                                for i in range(12):
                                    print(f"Tour {i + 1}/12")
                                    print("Player 1's Turn")
                                    dices = []
                                    for i in range(5):
                                        dices.append(randint(1, 6))
                                    print(f"2 Turns Left\nDices Rolled: {dices}")
                                    x = input("Reroll some dices? (y/n) ")
                                    if "y" in x.lower():
                                        y = input("Keep which ones?\nE.g. write \"0, 1, 3\" to reroll 1st, 2nd and 4th dices.\nWrite integers separated by commas to reroll them.\n")
                                        kk = f"[{y}]"
                                        for i in kk:
                                            dices = list(dices)
                                            dices[i] = randint(1, 6)
                                            dices = str(dices)
                                        print(f"1 Turns Left\nDices Rolled: {dices}")
                                        x = input("Reroll some dices? (y/n) ")
                                        if "y" in x.lower():
                                            y = input(
                                                "Keep which ones?\nE.g. write \"0, 1, 3\" to reroll 1st, 2nd and 4th dices.\nWrite integers separated by commas to reroll them.\n")
                                            kk = f"[{y}]"
                                            for i in kk:
                                                dices[i] = randint(1, 6)
                                            print(f"0 Turns Left\nDices Rolled: {dices}")
                                    print("Now select point type.")
                                    print("1 for upper section")
                                    print("2 for lower section")
                                    x = int(input("\n"))
                                    if x == 1:
                                        x = int(input("Write an integer 1-6 for aces-sixes. "))
                                        num = 0
                                        for i in dices:
                                            if i == x:
                                                num += x
                                        p1 += num
                                        print(f"{num} points added.")
                                    elif x == 2:
                                        print("1 for 3 of a kind")
                                        print("2 for 4 of a kind")
                                        print("3 for full house")
                                        print("4 for yahtzee")
                                        print("5 for small straight")
                                        print("6 for large straight")
                                        print("7 for chance")
                                        x = int(input("\n"))
                                        if x == 1:
                                            ofakind3 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 3:
                                                    ofakind3 = True
                                            if ofakind3:
                                                p1 += sum(dices)
                                                print(f"{sum(dices)} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 2:
                                            ofakind4 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 4:
                                                    ofakind4 = True
                                            if ofakind4:
                                                p1 += sum(dices)
                                                print(f"{sum(dices)} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 3:
                                            ofakind3 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 3:
                                                    ofakind3 = True
                                                    gai = dices[i]
                                            if ofakind3:
                                                while gai in dices:
                                                    for i in dices:
                                                        try:
                                                            if dices[i] == gai:
                                                                del dices[i]
                                                        except IndexError:
                                                            pass
                                            ofakind2 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 2:
                                                    ofakind2 = True
                                                    gai = dices[i]
                                            if ofakind2 and ofakind3:
                                                p1 += 50
                                                print(f"{50} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 4:
                                            if dices[1] == dices[2] and dices[2] == dices[3] and dices[3] == dices[4] and dices[4] == dices[5]:
                                                p1 += 25
                                                print(f"{25} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 5:
                                            dices.sort()
                                            if [1, 2, 3, 4] in dices or [2, 3, 4, 5] in dices or [3, 4, 5, 6] in dices:
                                                p1 += 30
                                                print(f"{30} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 6:
                                            dices.sort()
                                            if [1, 2, 3, 4, 5] in dices or [2, 3, 4, 5, 6] in dices:
                                                p1 += 40
                                                print(f"{40} points added.")
                                            else:
                                                p1 += 0
                                                print(f"{0} points added.")
                                        elif x == 7:
                                            p1 += sum(dices)
                                            print(f"{sum(dices)} added.")
                                    print("Player 2's Turn")
                                    dices = []
                                    for i in range(5):
                                        dices.append(randint(1, 6))
                                    print(f"2 Turns Left\nDices Rolled: {dices}")
                                    x = input("Reroll some dices? (y/n) ")
                                    if "y" in x.lower():
                                        y = input(
                                            "Keep which ones?\nE.g. write \"0, 1, 3\" to reroll 1st, 2nd and 4th dices.\nWrite integers separated by commas to reroll them.\n")
                                        kk = f"[{y}]"
                                        for i in kk:
                                            dices = list(dices)
                                            dices[i] = randint(1, 6)
                                            dices = str(dices)
                                        print(f"1 Turns Left\nDices Rolled: {dices}")
                                        x = input("Reroll some dices? (y/n) ")
                                        if "y" in x.lower():
                                            y = input(
                                                "Keep which ones?\nE.g. write \"0, 1, 3\" to reroll 1st, 2nd and 4th dices.\nWrite integers separated by commas to reroll them.\n")
                                            kk = f"[{y}]"
                                            for i in kk:
                                                dices = list(dices)
                                                dices[i] = randint(1, 6)
                                                dices = str(dices)
                                            print(f"0 Turns Left\nDices Rolled: {dices}")
                                    print("Now select point type.")
                                    print("1 for upper section")
                                    print("2 for lower section")
                                    x = int(input("\n"))
                                    if x == 1:
                                        x = int(input("Write an integer 1-6 for aces-sixes. "))
                                        num = 0
                                        for i in dices:
                                            if i == x:
                                                num += x
                                        p2 += num
                                        print(f"{num} points added.")
                                    elif x == 2:
                                        print("1 for 3 of a kind")
                                        print("2 for 4 of a kind")
                                        print("3 for full house")
                                        print("4 for yahtzee")
                                        print("5 for small straight")
                                        print("6 for large straight")
                                        print("7 for chance")
                                        x = int(input("\n"))
                                        if x == 1:
                                            ofakind3 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 3:
                                                    ofakind3 = True
                                            if ofakind3:
                                                p2 += sum(dices)
                                                print(f"{sum(dices)} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 2:
                                            ofakind4 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 4:
                                                    ofakind4 = True
                                            if ofakind4:
                                                p2 += sum(dices)
                                                print(f"{sum(dices)} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 3:
                                            ofakind3 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 3:
                                                    ofakind3 = True
                                                    gai = dices[i]
                                            if ofakind3:
                                                while gai in dices:
                                                    for i in dices:
                                                        try:
                                                            if dices[i] == gai:
                                                                del dices[i]
                                                        except IndexError:
                                                            pass
                                            ofakind2 = False
                                            for i in range(len(dices)):
                                                if dices.count(dices[i]) >= 2:
                                                    ofakind2 = True
                                                    gai = dices[i]
                                            if ofakind2 and ofakind3:
                                                p2 += 50
                                                print(f"{50} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 4:
                                            if dices[1] == dices[2] and dices[2] == dices[3] and dices[3] == dices[
                                                4] and dices[4] == dices[5]:
                                                p2 += 25
                                                print(f"{25} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 5:
                                            dices.sort()
                                            if [1, 2, 3, 4] in dices or [2, 3, 4, 5] in dices or [3, 4, 5, 6] in dices:
                                                p2 += 30
                                                print(f"{30} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 6:
                                            dices.sort()
                                            if [1, 2, 3, 4, 5] in dices or [2, 3, 4, 5, 6] in dices:
                                                p2 += 40
                                                print(f"{40} points added.")
                                            else:
                                                p2 += 0
                                                print(f"{0} points added.")
                                        elif x == 7:
                                            p2 += sum(dices)
                                            print(f"{sum(dices)} added.")
                            else:
                                break
                elif x == 5:
                    print("1 to open bingo")
                    print("2 to open data bank")
                    print("3 to open weather simulator")
                    print("4 to change the wordlist (used in word scramble e.t.c.)")
                    print("5 to open basic programs")
                    print("6 to open race simulator")
                    x = int(input("\n"))
                    if x == 1:
                        print("1 to open word bingo")
                        print("2 to open number bingo")
                        x = int(input("\n"))
                        if x == 1:
                            for i in range(5):
                                for i in range(5):
                                    print(choice(ohno), end = "  ")
                                print("\n")
                        elif x == 2:
                            for i in range(5):
                                for i in range(5):
                                    print(randint(0, 99), end = "   ")
                                print("\n")
                    elif x == 2:
                        print("1 to open Operating System data")
                        print("2 to open System data")
                        print("3 to open Sub-Process data")
                        print("4 to open Date and Time data")
                        print("5 to open Time data")
                        print("6 to open Math data")
                        print("7 to open more data")
                        x = int(input("\n"))
                        if x == 1:
                            print(f"Ex Ok: {EX_OK}")
                            print(f"F Ok: {F_OK}")
                            print(f"O Append: {O_APPEND}")
                            print(f"O Binary: {O_BINARY}")
                            print(f"O Creat: {O_CREAT}")
                            print(f"O Excl: {O_EXCL}")
                            print(f"O Noinherit: {O_NOINHERIT}")
                            print(f"O Random: {O_RANDOM}")
                            print(f"O Rdonly: {O_RDONLY}")
                            print(f"O Rdwr: {O_RDWR}")
                            print(f"O Sequential: {O_SEQUENTIAL}")
                            print(f"O Short Lived: {O_SHORT_LIVED}")
                            print(f"O Temporary: {O_TEMPORARY}")
                            print(f"O Text: {O_TEXT}")
                            print(f"O Trunc: {O_TRUNC}")
                            print(f"O Wronly: {O_WRONLY}")
                            print(f"P Detach: {P_DETACH}")
                            print(f"P Nowait: {P_NOWAIT}")
                            print(f"P Nowaito: {P_NOWAITO}")
                            print(f"P Overlay: {P_OVERLAY}")
                            print(f"P Wait: {P_WAIT}")
                            print(f"R Ok: {R_OK}")
                            print(f"Seek Cur: {SEEK_CUR}")
                            print(f"Seek End: {SEEK_END}")
                            print(f"Seek Set: {SEEK_SET}")
                            print(f"Tmp Max: {TMP_MAX}")
                            print(f"W Ok: {W_OK}")
                            print(f"X Ok: {X_OK}")
                            print(f"Altsep: {altsep}")
                            print(f"Curdir: {curdir}")
                            print(f"Defpath: {defpath}")
                            print(f"Devnull: {devnull}")
                            print(f"Environ: {environ}")
                            print(f"Extsep: {extsep}")
                            print(f"Linesep: {linesep}")
                            print(f"Name: {name}")
                            print(f"Pardir: {pardir}")
                            print(f"Pathsep: {pathsep}")
                            print(f"Sep: {sep}")
                            print(f"Supports Bytes Environ: {supports_bytes_environ}")
                        elif x == 2:
                            print(f"Stderr: {__stderr__}")
                            print(f"Stdin: {__stdin__}")
                            print(f"Stdout: {__stdout__}")
                            print(f"API Version: {api_version}")
                            print(f"Argv: {argv}")
                            print(f"Base Exec Prefix: {base_exec_prefix}")
                            print(f"Base Prefix: {base_prefix}")
                            print(f"Builtin Module Names: {builtin_module_names}")
                            print(f"Byteorder: {byteorder}")
                            print(f"Copyright: {copyright}")
                            print(f"DLL Handle: {dllhandle}")
                            print(f"Dont Write Bytecode: {dont_write_bytecode}")
                            print(f"Exec Prefix: {exec_prefix}")
                            print(f"Executable: {executable}")
                            print(f"Flags: {flags}")
                            print(f"Float Info: {float_info}")
                            print(f"Float Repr Style: {float_repr_style}")
                            print(f"Hash Info: {hash_info}")
                            print(f"Hex Version: {hexversion}")
                            print(f"Implementation: {implementation}")
                            print(f"Int Info: {int_info}")
                            print(f"Maxsize: {maxsize}")
                            print(f"Maxunicode: {maxunicode}")
                            print(f"Meta Path: {meta_path}")
                            print(f"Modules: {modules}")
                            print(f"Orig Argv: {orig_argv}")
                            print(f"Path: {path}")
                            print(f"Path Hooks: {path_hooks}")
                            print(f"Path Importer Cache: {path_importer_cache}")
                            print(f"Platform: {platform}")
                            print(f"Platlibdir: {platlibdir}")
                            print(f"Prefix: {prefix}")
                            print(f"Pycache Prefix: {pycache_prefix}")
                            print(f"Stderr: {stderr}")
                            print(f"Stdin: {stdin}")
                            print(f"Stdlib Module Names: {stdlib_module_names}")
                            print(f"Stdout: {stdout}")
                            print(f"Thread Info: {thread_info}")
                            print(f"Version: {version}")
                            print(f"Version Info: {version_info}")
                            print(f"Warnoptions: {warnoptions}")
                            print(f"Winver: {winver}")
                        elif x == 3:
                            print(f"Above Normal Priority Class: {ABOVE_NORMAL_PRIORITY_CLASS}")
                            print(f"Below Normal Priority Class: {BELOW_NORMAL_PRIORITY_CLASS}")
                            print(f"Create Breakaway From Job: {CREATE_BREAKAWAY_FROM_JOB}")
                            print(f"Create Default Error Mode: {CREATE_DEFAULT_ERROR_MODE}")
                            print(f"Create New Console: {CREATE_NEW_CONSOLE}")
                            print(f"Create New Process Group: {CREATE_NEW_PROCESS_GROUP}")
                            print(f"Create No Window: {CREATE_NO_WINDOW}")
                            print(f"Detached Process: {DETACHED_PROCESS}")
                            print(f"Devnull: {DEVNULL}")
                            print(f"High Priority Class: {HIGH_PRIORITY_CLASS}")
                            print(f"Idle Priority Class: {IDLE_PRIORITY_CLASS}")
                            print(f"Normal Priority Class: {NORMAL_PRIORITY_CLASS}")
                            print(f"Pipe: {PIPE}")
                            print(f"Realtime Priority Class: {REALTIME_PRIORITY_CLASS}")
                        elif x == 4:
                            print(f"Now: {datetime.now()}")
                            print(f"Max Year: {MAXYEAR}")
                            print(f"Min Year: {MINYEAR}")
                            print(f"UTC: {UTC}")
                        elif x == 5:
                            print(f"Altzone: {altzone}")
                            print(f"Daylight: {daylight}")
                            print(f"Timezone: {timezone}")
                            print(f"Tzname: {tzname}")
                        elif x == 6:
                            print(f"E: {e}")
                            print(f"Inf: {inf}")
                            print(f"NaN: {nan}")
                            print(f"Pi: {pi}")
                            print(f"Tau: {tau}")
                        elif x == 7:
                            print("1 to open Mathematics Plot Library data")
                            print("2 to open Urwid data")
                            print("3 to open the Zen of Python data")
                            print("4 to open Command Prompt data")
                            x = int(input("\n"))
                            if x == 1:
                                print(f"__Bibtex__: {__bibtex__}")
                                print(f"Bivar Colormaps: {bivar_colormaps}")
                                print(f"Color Sequences: {color_sequences}")
                                print(f"Colormaps: {colormaps}")
                                print(f"Default Params: {defaultParams}")
                                print(f"Multivar Colormaps: {multivar_colormaps}")
                                print(f"RcParams: {rcParams}")
                                print(f"RcParams Default: {rcParamsDefault}")
                                print(f"RcParams Orig: {rcParamsOrig}")
                            elif x == 2:
                                print(f"Activate: {ACTIVATE}")
                                print(f"Any: {ANY}")
                                print(f"Black: {BLACK}")
                                print(f"Bottom: {BOTTOM}")
                                print(f"Box: {BOX}")
                                print(f"Brown: {BROWN}")
                                print(f"Center: {CENTER}")
                                print(f"Clip: {CLIP}")
                                print(f"Cursor Down: {CURSOR_DOWN}")
                                print(f"Cursor Left: {CURSOR_LEFT}")
                                print(f"Cursor Max Left: {CURSOR_MAX_LEFT}")
                                print(f"Cursor Max Right: {CURSOR_MAX_RIGHT}")
                                print(f"Cursor Page Down: {CURSOR_PAGE_DOWN}")
                                print(f"Cursor Page Up: {CURSOR_PAGE_UP}")
                                print(f"Cursor Right: {CURSOR_RIGHT}")
                                print(f"Cursor Up: {CURSOR_UP}")
                                print(f"Dark Blue: {DARK_BLUE}")
                                print(f"Dark Cyan: {DARK_CYAN}")
                                print(f"Dark Gray: {DARK_GRAY}")
                                print(f"Dark Green: {DARK_GREEN}")
                                print(f"Dark Magenta: {DARK_MAGENTA}")
                                print(f"Dark Red: {DARK_RED}")
                                print(f"Default: {DEFAULT}")
                                print(f"Ellipsis: {ELLIPSIS}")
                                print(f"Fixed: {FIXED}")
                                print(f"Flow: {FLOW}")
                                print(f"Given: {GIVEN}")
                                print(f"Left: {LEFT}")
                                print(f"Light Blue: {LIGHT_BLUE}")
                                print(f"Light Cyan: {LIGHT_CYAN}")
                                print(f"Light Gray: {LIGHT_GRAY}")
                                print(f"Light Green: {LIGHT_GREEN}")
                                print(f"Light Magenta: {LIGHT_MAGENTA}")
                                print(f"Light Red: {LIGHT_RED}")
                                print(f"Middle: {MIDDLE}")
                                print(f"Pack: {PACK}")
                                print(f"Redraw Screen: {REDRAW_SCREEN}")
                                print(f"Relative: {RELATIVE}")
                                print(f"Relative 100: {RELATIVE_100}")
                                print(f"Right: {RIGHT}")
                                print(f"Space: {SPACE}")
                                print(f"Top: {TOP}")
                                print(f"Update Palette Entry: {UPDATE_PALETTE_ENTRY}")
                                print(f"Version: {VERSION}")
                                print(f"Weight: {WEIGHT}")
                                print(f"White: {WHITE}")
                                print(f"Yellow: {YELLOW}")
                                print(f"__Annotations__: {__annotations__}")
                                print(f"__Version Tuple__: {__version_tuple__}")
                                print(f"Command Map: {command_map}")
                                print(f"Default Layout: {default_layout}")
                                print(f"Detected Encoding: {detected_encoding}")
                            elif x == 3:
                                print(f"C: {c}")
                                print(f"D: {d}")
                                print(f"I: {i}")
                                print(f"S: {s}")
                            elif x == 4:
                                for i in echo:
                                    print(i)
                                    system(i)
                                x = input("Open tree data?\nWarning: data overflow can happen!\n(y/n) ")
                                if "y" in x.lower():
                                    print("tree")
                                    system("tree \\")
                    elif x == 3:
                        x = int(input("How many entries? "))
                        print("Day #1")
                        print(f"Weather: {selectedw}")
                        print(f"Temprature: {temp} °C")
                        for i in range(x - 1):
                            if randint(1, 2) == 1:
                                selectedw = choice(weather)
                            temp = temp + randint(-2, 2)
                            print(f"Day #{i + 2}")
                            print(f"Weather: {selectedw}")
                            print(f"Temprature: {temp} °C")
                    elif x == 4:
                        print("1 to add word")
                        print("2 to remove word")
                        print("3 to manually change")
                        x = int(input("\n"))
                        if x == 1:
                            x = input("Add which word? ")
                            if x in ohno:
                                print("Word already included.")
                            else:
                                ohno.append(x)
                        elif x == 2:
                            x = input("Remove which word? ")
                            if x in ohno:
                                del ohno[ohno.index(x)]
                            else:
                                print("Word already removed.")
                        elif x == 3:
                            x = input("Please enter what will the text now look like as a Python list data type:\n")
                            ohno = x
                    elif x == 5:
                        print("1 to open Hello World")
                        print("2 to open cat")
                        print("3 to open looping counter")
                        print("4 to open truth machine")
                        print("5 to open XKCD Random Number")
                        print("6 to open Quine")
                        print("7 to find prime numbers")
                        print("8 to print the fibonacci sequence")
                        print("9 to print powers of 2")
                        print("10 to open FizzBuzz")
                        print("11 to open 99 Bottles of Beer")
                        print("12 to open more complicated programs")
                        x = int(input("\n"))
                        if x == 1:
                            print("Hello, World!")
                        elif x == 2:
                            x = input("Enter text: ")
                            print(x)
                        elif x == 3:
                            x = 0
                            y = int(input("Print how many times? "))
                            for i in range(y):
                                print(x)
                                x += 1
                        elif x == 4:
                            x = int(input("Enter number: "))
                            if x == 1:
                                while True:
                                    print(x)
                            elif x == 0:
                                print(x)
                        elif x == 5:
                            print(4) # chosen by a fair roll
                        elif x == 6:
                            s = 's = {!r}\nprint(s.format(s))'
                            print(s.format(s))
                        elif x == 7:
                            x = 2
                            y = int(input("Print how many times? "))
                            print(0)
                            print(1)
                            for i in range(y - 2):
                                prime = True
                                print(x, end="")
                                for i in range(2, int(x ** 0.5) + 1):
                                    if x % i == 0:
                                        prime = False
                                        break
                                if prime:
                                    print(" prime")
                                else:
                                    print("")
                                x += 1
                        elif x == 8:
                            y = int(input("Print how many times? "))
                            fib1 = 0
                            fib2 = 1
                            print(0)
                            print(1)
                            for i in range(y - 2):
                                fib3 = fib1
                                fib4 = fib2
                                print(fib1 + fib2)
                                fib1 = fib4
                                fib2 = fib3 + fib4
                        elif x == 9:
                            x = int(input("Print how many times? "))
                            pow = 1
                            for i in range(x):
                                print(pow)
                                pow *= 2
                        elif x == 10:
                            x = int(input("Print how many times? "))
                            for i in range(x):
                                if i % 3 == 0 and i % 5 == 0:
                                    print(f"FizzBuzz ({i})")
                                elif i % 3 == 0:
                                    print(f"Fizz ({i})")
                                elif i % 5 == 0:
                                    print(f"Buzz ({i})")
                                else:
                                    print(i)
                        elif x == 11:
                            for i in range(99, 0, -1):
                                print(f"{i} bottles of beer on the wall!")
                                print(f"{i} bottles of beer!")
                                print("Take one down, pass it around")
                                print(f"{i - 1} bottles of beer on the wall!")
                        elif x == 12:
                            print("1 to open speed by gallons management")
                            print("2 to open credit card limit management")
                            print("3 to open interest charge management")
                            print("4 to open salary management")
                            print("5 to open number guessing")
                            x = int(input("\n"))
                            if x == 1:
                                avr = []
                                print("Please write \"q\" to the \"gallons used\" part to quit.")
                                while True:
                                    x = input("Enter gallons used: ")
                                    if x.lower() == "q": break
                                    else: x = float(x)
                                    y = float(input("Enter km's driven: "))
                                    z = y / x
                                    print(f"Km/g for this truck is {z}.")
                                    avr.append(z)
                                avr = sum(avr) / len(avr)
                                print(f"Average km/g is {avr}.")
                            elif x == 2:
                                print("Please write \"q\" to \"account number\" to quit.")
                                while True:
                                    x = input("Account number: ")
                                    if x.lower() == "q": break
                                    y = float(input("Beginning balance: "))
                                    z = float(input("Total charges: "))
                                    a = float(input("Total credits: "))
                                    b = float(input("Credit limit: "))
                                    c = y + z - a
                                    print(f"Balance: ${c}")
                                    if c > b:
                                        print("Credit limit exceeded.")
                                    else:
                                        print("Credit limit didn't exceed.")
                            elif x == 3:
                                print("Please write \"q\" to the \"loan principal\" part to quit.")
                                while True:
                                    x = input("Enter loan principal: ")
                                    if x.lower() == "q": break
                                    else: x = float(x)
                                    y = float(input("Enter interest rate: "))
                                    z = float(input("Enter term of the loan (days): "))
                                    a = x * y * z / 365
                                    print(f"The interest charge is {a}.")
                            elif x == 4:
                                avr = []
                                print("Please write \"q\" to the \"hours worked\" part to quit.")
                                while True:
                                    x = input("Enter hours worked: ")
                                    if x.lower() == "q": break
                                    else: x = float(x)
                                    y = float(input("Enter hourly rate: "))
                                    z = x / y
                                    print(f"Salary is ${z}.")
                                    avr.append(z)
                                avr = sum(avr) / len(avr)
                                print(f"Average salary is ${avr}.")
                            elif x == 5:
                                print("Please enter the number range.")
                                a = int(input("Minimum Number: "))
                                b = int(input("Maximum Number: "))
                                while True:
                                    x = randint(a, b)
                                    print("Number selected")
                                    y = ""
                                    z = 1
                                    while y != x:
                                        y = int(input("Guess the number: "))
                                        if y == x:
                                            x = input(f"You guessed correctly!\nTry again? (y/n) ")
                                            if not("y" in x.lower()): break
                                        else:
                                            z += 1
                                            if y < x:
                                                print("The number is too low.")
                                            else:
                                                print("The number is too high.")
                    elif x == 6:
                        print("Welcome to the race of tortoise and hare!")
                        print("Each start at the 1st metre of the 70 m race.")
                        input("Shall the race begin? ")
                        i = float(input("And the interval between each move? "))
                        t = 1
                        h = 1
                        while True:
                            print(f"Tortoise: {t} m")
                            print(f"Hare: {h} m")
                            if randint(1, 100) <= 50:
                                print("The tortoise did a fast plod!")
                                t += 3
                            elif randint(1, 50) <= 20:
                                print("The tortoise did a slip!")
                                t -= 6
                            else:
                                print("The tortoise did a slow plod!")
                                t += 1
                            if randint(1, 100) <= 20:
                                print("The hare did a sleep!")
                            elif randint(1, 80) <= 20:
                                print("The hare did a big hop!")
                                h += 9
                            elif randint(1, 60) <= 10:
                                print("The hare did a big slip!")
                                h -= 12
                            elif randint(1, 50) <= 30:
                                print("The hare did a small hop!")
                                h += 1
                            else:
                                print("The hare did a small slip!")
                                h -= 2
                            if t < 0:
                                t = 0
                                print("The tortoise is still at the start!")
                            elif t >= 70:
                                print("The tortoise won!!!")
                                break
                            if h < 0:
                                print("The hare is still at the start!")
                                h = 0
                            elif h >= 70:
                                print("The hare won!")
                                break
                            sleep(i)
                            print()
        elif x == 2:
            print("1 to open calculator")
            print("2 to open gallery")
            print("3 to open notebook")
            print("4 to open to-do")
            print("5 to open paint")
            print("6 to open puzzle")
            print("7 to open clock")
            print("8 to open snake")
            print("9 to open sudoku")
            print("10 to open minesweeper")
            print("11 to open solitaire")
            print("12 to open code scraps")
            x = int(input("\n"))
            if x == 1:
                print("1 to open normal calculator")
                print("2 to open calculator with variety")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.calculator.net/")
                elif x == 2:
                    web("https://www.desmos.com/")
            elif x == 2:
                print("1 to open photo gallery")
                print("2 to open image gallery")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.flickr.com/")
                elif x == 2:
                    web("https://freepik.com/")
            elif x == 3:
                print("1 to open notebook")
                print("2 to open notepad")
                x = int(input("\n"))
                if x == 1:
                    web("https://onlinenotepad.org/app")
                elif x == 2:
                    web("https://onlinenotepad.org/notepad")
            elif x == 4:
                web("https://flask.io/")
            elif x == 5:
                web("https://jspaint.app/")
            elif x == 6:
                print("1 to open jigsaw")
                print("2 to open tiles")
                print("3 to open daily puzzles")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.jigsawplanet.com/")
                elif x == 2:
                    web("https://slidingtiles.com/")
                elif x == 3:
                    web("https://trainwrecklabs.com/")
            elif x == 7:
                print("1 to open clock")
                print("2 to open alarm")
                print("3 to open stopwatch")
                print("4 to open timer")
                print("5 to open calendar")
                x = int(input("\n"))
                if x == 1:
                    web("https://time.is/")
                elif x == 2:
                    web("https://vclock.com/")
                elif x == 3:
                    web("https://www.online-stopwatch.com/")
                elif x == 4:
                    web("https://www.timeanddate.com/timer/")
                elif x == 5:
                    web("https://www.timeanddate.com/calendar/")
            elif x == 8:
                print("1 to open general snake")
                print("2 to open maps snake")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.google.com/search?q=snake")
                elif x == 2:
                    input("Website Closed")
                    web("https://snake.googlemaps.com/")
            elif x == 9:
                web("https://sudoku.com/")
            elif x == 10:
                print("1 to open Google minesweeper")
                print("2 to open minesweeper")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.google.com/search?q=minesweeper")
                elif x == 2:
                    web("https://minesweeper.online/")
            elif x == 11:
                print("1 to open Google solitaire")
                print("2 to open solitaire")
                x = int(input("\n"))
                if x == 1:
                    web("https://www.google.com/search?q=solitaire")
                elif x == 2:
                    web("https://solitaired.com/")
            elif x == 12:
                print("1 to open jukebox")
                print("2 to open piano")
                print("3 to open budget manager")
                print("4 to open logic evaluator")
                print("5 to open vocabulary")
                print("6 to open roulette")
                x = int(input("\n"))
                if x == 1:
                    print("1 to open music")
                    print("2 to open jukebox")
                    print("3 to open music editor")
                    x = int(input("\n"))
                    if x == 1:
                        web("https://open.spotify.com/")
                    elif x == 2:
                        web("https://jukebox.today/")
                    elif x == 3:
                        print("1 for normal editor")
                        print("2 for cartoony editor")
                        x = int(input("\n"))
                        if x == 1:
                            web("https://audiomass.co/")
                        elif x == 2:
                            web("https://danielx.net/composer/")
                elif x == 2:
                    web("https://www.musicca.com/piano")
                elif x == 3:
                    web("https://moneysmart.gov.au/budgeting/budget-planner")
                elif x == 4:
                    web("https://logic.ly/demo/")
                elif x == 5:
                    web("https://www.vocabulary.com/")
                elif x ==6:
                    web("https://www.247games.com/roulette/")
        """
        app list:
        calculator
        gallery
        notebook
        to-do
        paint
        puzzle
        clock
        snake
        sudoku
        minesweeper
        solitaire
        """
    elif x == 2:
        print("1 to convert Unicode to character")
        print("2 to convert character to Unicode")
        print("3 to list unicode")
        print("4 to cipher words")
        print("5 to open Unicode index list")
        x = int(input("\n"))
        if x == 1:
            x = int(input("Enter Unicode number: "))
            print(f"Decoded character: {chr(x)}")
        elif x == 2:
            x = input("Enter character: ")
            print(f"Encoded number: {ord(x)}")
        elif x == 3:
            print("1 to list unicode with numbers")
            print("2 to list unicode normally")
            print("3 to list unicode randomly with numbers")
            print("4 to list unicode random normally")
            x = int(input("\n"))
            y = int(input("List how many unicode? "))
            if x == 1 or x == 3:
                z = input("What should be written between the number and Unicode? ")
            if x == 1:
                for i in range(y):
                    print(f"{i}{z}{chr(i)}")
            elif x == 2:
                a = int(input("List how many unicode per line? "))
                for i in range(y):
                    print(chr(i), end="")
                    if i % a == 0:
                        print()
                print()
            elif x == 3:
                for i in range(y):
                    j = randint(0, 55295)
                    print(f"{j}{z}{chr(j)}")
            elif x == 4:
                for i in range(y):
                    j = randint(0, 55295)
                    print(chr(j), end="")
        elif x == 4:
            print("1 to cipher words in Caesar Cipher using ASCII")
            print("2 to cipher words in any type")
            x = int(input("\n"))
            if x == 1:
                x = input(
                    "Please give the type of Caesar cipher you want.\nE.g. for \"Caesar +3\" cipher, write \"+3\".\n")
                y = input(f"Word to cipher with Caesar {x}: ")
                list = []
                for i in range(len(y)):
                    list.append(y[i])
                for i in range(len(list)):
                    list[i] = eval(f"chr(ord(list[i]) {x})")
                y = ""
                for i in list:
                    y = f"{y}{i}"
                print(y)
            elif x == 2:
                print("Enter the cipher type. (e.g. \"rot_13\" for Rot13 cipher, basically \"codecs.encode(obj, encoding)\" function.")
                x = input("Get information about that function? (y/n) ")
                if "y" in x.lower():
                    help("codecs.encode")
                x = input("Cipher type: ")
                y = input("Word to cipher: ")
                encode(y, x)
        elif x == 5:
            print("Common ASCII")
            print("0-31   Unknown ASCII codes")
            print("32     Whitespace")
            print("33-47  Casual Symbols")
            print("48-57  Integers")
            print("58-64  Uncommon Symbols")
            print("65-90  Uppercase Latin Letters")
            print("91-96  Rare Symbols")
            print("97-122 Lowercase Latin Letters")
            print("Uncommon ASCII")
            print("123-126 Rarer Symbols")
            print("127-160 Unknown ASCII")
            print("161-191 Random Symbols")
            print("192-696 Foreign Latin Letters")
            print("697-885 Quotation")
            print("Rare ASCII")
            print("886-13620 Random Foreign Letters and Symbols")
            print("ASCII Far Lands")
            print("13621-20153 Chinese Letters Vol. 1")
            print("20154-20176 Japanese Letters")
            print("20177-23454 Random East Asian Letters")
            print("23455-40959 Chinese Letters Vol. 2")
            print("ASCII Farther Lands")
            print("40960-43647 Random Letters")
            print("43648-44031 Patch of Unknown ASCII")
            print("44032-55203 Chinese Letters Vol. 3")
            print("ASCII Farthest Lands")
            print("55204-55215 More Unknown ASCII")
            print("55216-55242 Alphabet of Random Lines")
            print("55243-55291 Lowercase AoRL")
            print("The End of ASCII")
            print("55292-55294 Some Unknown Symbols")
            print("55295       The Last ASCII character")
            print("ASCII Further Lands")
            print("55296-??? The Undiscovered")
    elif x == 3:
        print("1 to open Python")
        print("2 to open Python Documentation")
        print("3 to open code console")
        print("4 to get operating system information")
        print("5 to operate system")
        print("6 to read FOS readme.txt")
        print("7 to get syntax list for Python")
        print("8 to open OS shell")
        print("9 to use sorting algorithms")
        print("10 to open the Zen of Python")
        print("11 to print text")
        print("12 to manage modules")
        print("13 to open programming hall of fame")
        print("14 to open infinite writing space")
        x = int(input("\n"))
        if x == 1:
            web("https://www.python.org/")
        elif x == 2:
            print("1 to open in local wireless")
            print("2 to open in online")
            x = int(input("\n"))
            if x == 1:
                print("1 to manually get documentation")
                print("2 to get documentation-based Python tutorial")
                print("3 to open documentation shell")
                print("4 to search in Python libraries")
                print("5 to get random documentation")
                x = int(input("\n"))
                if x == 1:
                    print("1 to open Python documentation")
                    print("2 to open Batch documentation")
                    x = int(input("\n"))
                    if x == 1:
                        x = input(">>> ")
                        help(x)
                    elif x == 2:
                        x = input(">>> ")
                        system(f"help {x}")
                elif x == 2:
                    print("Vol. I - Data Types")
                    print("Vol. II - Standard Input-Output")
                    print("Vol. III - Statements")
                    print("Vol. IV - Defining")
                    print("Vol. V - Modules")
                    print("Vol. VI - Pip Packages and Batch")
                    print("Vol. VII - Python Standard Library")
                    print("Vol. VIII - The Zen of Python")
                    print("Vol. IX - Code Execution")
                    print("Vol. X - File Handling")
                    x = int(input())
                    if x == 1:
                        print("Vol. I - Normal Data Types")
                        print("Vol. II - Plural Data Types")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - Strings")
                            print("Vol. II - Numbers")
                            print("Vol. III - Boolean Values")
                            print("Vol. IV - Topic")
                            x = int(input())
                            if x == 1:
                                print("Vol. I - Data Type")
                                print("Vol. II - Topic")
                                x = int(input())
                                if x == 1:
                                    help("str")
                                elif x == 2:
                                    print("Vol. I - Main")
                                    print("Vol. II - Methods")
                                    x = int(input())
                                    if x == 1:
                                        help("STRINGS")
                                    elif x == 2:
                                        help("STRINGMETHODS")
                            elif x == 2:
                                print("Vol. I - Integers")
                                print("Vol. II - Float Values")
                                print("Vol. III - Arithmetic")
                                print("Vol. IV - Topic")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("int")
                                    elif x == 2:
                                        help("INTEGER")
                                elif x == 2:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("float")
                                    elif x == 2:
                                        help("FLOAT")
                                elif x == 3:
                                    print("Vol. I - Addition")
                                    print("Vol. II - Subtraction")
                                    print("Vol. III - Multiplication")
                                    print("Vol. IV - Division")
                                    print("Vol. V - Modulo")
                                    print("Vol. VI - Exponentation")
                                    print("Vol. VII - Floor Division")
                                    x = int(input())
                                    if x == 1:
                                        help("+")
                                    elif x == 2:
                                        help("-")
                                    elif x == 3:
                                        help("*")
                                    elif x == 4:
                                        help("/")
                                    elif x == 5:
                                        help("%")
                                    elif x == 6:
                                        help("**")
                                    elif x == 7:
                                        help("//")
                            elif x == 3:
                                print("Vol. I - Data Type")
                                print("Vol. II - Boolean Logic Operators")
                                print("Vol. III - Boolean Logic Values")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("bool")
                                    elif x == 2:
                                        help("BOOLEAN")
                                elif x == 2:
                                    print("Vol. I - Logic Symbols")
                                    print("Vol. II - Logical Operators")
                                    x = int(input())
                                    if x == 1:
                                        print("Vol. I - Equal to")
                                        print("Vol. II - Greater than")
                                        print("Vol. III - Less than")
                                        x = int(input())
                                        if x == 1:
                                            print("Vol. I - Equal to")
                                            print("Vol. II - Not Equal to")
                                            x = int(input())
                                            if x == 1:
                                                help("==")
                                            elif x == 2:
                                                help("!=")
                                        elif x == 2:
                                            print("Vol. I - Greater than")
                                            print("Vol. II - Greater than or Equal to")
                                            x = int(input())
                                            if x == 1:
                                                help(">")
                                            elif x == 2:
                                                help(">=")
                                        elif x == 3:
                                            print("Vol. I - Less than")
                                            print("Vol. II - Less than or Equal to")
                                            x = int(input())
                                            if x == 1:
                                                help("<")
                                            elif x == 2:
                                                help("<=")
                                    elif x == 2:
                                        print("Vol. I - And (Both needs to be true)")
                                        print("Vol. II - Or (One needs to be true)")
                                        print("Vol. III - Not (Opposite of given statement)")
                                        x = int(input())
                                        if x == 1:
                                            help("and")
                                        elif x == 2:
                                            help("or")
                                        elif x == 3:
                                            help("not")
                                elif x == 3:
                                    print("Vol. 1 - 1 (True)")
                                    print("Vol. 2 - 0 (False)")
                                    x = int(input())
                                    if x == 1:
                                        help("True")
                                    elif x == 2:
                                        help("False")
                            elif x == 4:
                                print("Vol. I - Data Types")
                                print("Vol. II - Type Objects")
                                x = int(input())
                                if x == 1:
                                    help("TYPES")
                                elif x == 2:
                                    help("TYPEOBJECTS")
                        elif x == 2:
                            print("Vol. I - Lists")
                            print("Vol. II - Tuples")
                            print("Vol. III - Dictionaries")
                            x = int(input())
                            if x == 1:
                                print("Vol. I - Data Type")
                                print("Vol. II - Brackets")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("list")
                                    elif x == 2:
                                        print("Vol. I - Lists")
                                        print("Vol. II - List Literals")
                                        x = int(input())
                                        if x == 1:
                                            help("LISTS")
                                        elif x == 2:
                                            help("LISTLITERALS")
                                elif x == 2:
                                    print("Vol. I - Opening Bracket ([)")
                                    print("Vol. II - Closing Bracket (])")
                                    x = int(input())
                                    if x == 1:
                                        help("[")
                                    elif x == 2:
                                        help("]")
                            elif x == 2:
                                print("Vol. I - Data Type")
                                print("Vol. II - Brackets")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Brackets")
                                    x = int(input())
                                    if x == 1:
                                        print("Vol. I - Data Type")
                                        print("Vol. II - Topic")
                                        x = int(input())
                                        if x == 1:
                                            help("tuple")
                                        elif x == 2:
                                            print("Vol. I - Tuples")
                                            print("Vol. II - Tuple Literals")
                                            x = int(input())
                                            if x == 1:
                                                help("TUPLES")
                                            elif x == 2:
                                                help("TUPLELITERALS")
                                elif x == 2:
                                    print("Vol. I - Opening Bracket (()")
                                    print("Vol. II - Closing Bracket ())")
                                    x = int(input())
                                    if x == 1:
                                        help("(")
                                    elif x == 2:
                                        help(")")
                            elif x == 3:
                                print("Vol. I - Data Type")
                                print("Vol. II - Brackets")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("dict")
                                    elif x == 2:
                                        print("Vol. I - Dictionaries")
                                        print("Vol. II - Dictionary Literals")
                                        x = int(input())
                                        if x == 1:
                                            help("DICTIONARIES")
                                        elif x == 2:
                                            help("DICTIONARYLITERALS")
                    if x == 2:
                        print("Vol. I - Input")
                        print("Vol. II - Output")
                        x = int(input())
                        if x == 1:
                            help("input")
                        elif x == 2:
                            help("print")
                    elif x == 3:
                        print("Vol. I - Boolean Logic Statements")
                        print("Vol. II - While Statements")
                        print("Vol. III - Repeat Statements")
                        print("Vol. IV - Topic")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - If-Then")
                            print("Vol. II - If-Else")
                            print("Vol. III - If-Else-If")
                            x = int(input())
                            if x == 1:
                                help("if")
                            elif x == 2:
                                help("else")
                            elif x == 3:
                                help("elif")
                        elif x == 2:
                            help("while")
                        elif x == 3:
                            print("Vol. I - For Syntax")
                            print("Vol. II - In Syntax")
                            print("Vol. III - Range Syntax")
                            x = int(input())
                            if x == 1:
                                help("for")
                            elif x == 2:
                                help("in")
                            elif x == 3:
                                help("range")
                        elif x == 4:
                            help("LOOPING")
                    elif x == 4:
                        print("Vol. I - Functions")
                        print("Vol. II - Classes and Polymorphism")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - Defining")
                            print("Vol. II - Brackets")
                            x = int(input())
                            if x == 1:
                                print("Vol. I - Data Type")
                                print("Vol. II - Brackets")
                                x = int(input())
                                if x == 1:
                                    print("Vol. I - Data Type")
                                    print("Vol. II - Topic")
                                    x = int(input())
                                    if x == 1:
                                        help("list")
                                    elif x == 2:
                                        print("Vol. I - Defining")
                                        print("Vol. II - Topic")
                                        x = int(input())
                                        if x == 1:
                                            help("def")
                                        elif x == 2:
                                            help("FUNCTIONS")
                            elif x == 2:
                                print("Vol. I - Opening Bracket (()")
                                print("Vol. II - Closing Bracket ())")
                                x = int(input())
                                if x == 1:
                                    help("(")
                                elif x == 2:
                                    help(")")
                        elif x == 2:
                            print("Vol. I - Defining")
                            print("Vol. II - Topic")
                            x = int(input())
                            if x == 1:
                                help("class")
                            elif x == 2:
                                help("CLASSES")
                    if x == 5:
                        print("Vol. I - Module Importing")
                        print("Vol. II - Module Function List")
                        print("Vol. III - Basic Modules")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - Importing Normally")
                            print("Vol. II - \"From\" Statement")
                            print("Vol. III -  Topic")
                            x = int(input())
                            if x == 1:
                                help("import")
                            elif x == 2:
                                help("from")
                            elif x == 3:
                                help("IMPORTING")
                        elif x == 2:
                            help("dir")
                        elif x == 3:
                            print("Vol. I - Operating System")
                            print("Vol. II - Date and Time")
                            print("Vol. III - Calendar")
                            print("Vol. IV - Sub-Process")
                            print("Vol. V - Web Browser")
                            print("Vol. VI - Random")
                            print("Vol. VII - Math")
                            print("Vol. VIII - Statistics")
                            x = int(input())
                            if x == 1:
                                print("Vol. I - Main")
                                print("Vol. II - Name")
                                x = int(input())
                                if x == 1:
                                    help("os")
                                elif x == 2:
                                    help("os.name")
                            elif x == 2:
                                print("Vol. I - Main")
                                print("Vol. II - Date")
                                x = int(input())
                                if x == 1:
                                    help("datetime")
                                elif x == 2:
                                    help("datetime.datetime.name")
                            elif x == 3:
                                print("Vol. I - Main")
                                print("Vol. II - Calendar Defining")
                                print("Vol. III - Calendar Writing")
                                x = int(input())
                                if x == 1:
                                    help("calendar")
                                elif x == 2:
                                    help("calendar.TextCalendar")
                                elif x == 3:
                                    print("Vol. I - Monthly Calendar")
                                    print("Vol. II - Yearly Calendar")
                                    x = int(input())
                                    if x == 1:
                                        help("calendar.TextCalendar.prmonth")
                                    elif x == 2:
                                        help("calendar.TextCalendar.pryear")
                            elif x == 4:
                                print("Vol. I - Main")
                                print("Vol. II - File Opening")
                                print("Vol. III - I.P. Address Pinging")
                                x = int(input())
                                if x == 1:
                                    help("subprocess")
                                elif x == 2:
                                    help("subprocess.call")
                                elif x == 3:
                                    print("Vol. I - Pinging")
                                    print("Vol. II - Waiting")
                                    print("Vol. III - Polling")
                                    x = int(input())
                                    if x == 1:
                                        help("subprocess.Popen")
                                    elif x == 2:
                                        help("subprocess.Popen.wait")
                                    elif x == 3:
                                        help("subprocess.Popen.poll")
                            elif x == 5:
                                print("Vol. I - Main")
                                print("Vol. II - URL Opening")
                                x = int(input())
                                if x == 1:
                                    help("webbrowser")
                                elif x == 2:
                                    help("webbrowser.open")
                            elif x == 6:
                                print("Vol. I - Main")
                                print("Vol. II - Random Decimal")
                                print("Vol. III - Random Integer")
                                print("Vol. IV - Random Element from List")
                                print("Vol. V - Random Data from Normal Distribution")
                                x = int(input())
                                if x == 1:
                                    help("random")
                                elif x == 2:
                                    help("random.random")
                                elif x == 3:
                                    help("random.randint")
                                elif x == 4:
                                    help("random.choice")
                                elif x == 5:
                                    print("Vol. I - Gauss Distribution")
                                    print("Vol. II - Normal Variate")
                                    x = int(input())
                                    if x == 1:
                                        help("random.gauss")
                                    elif x == 2:
                                        help("random.normalvariate")
                            elif x == 7:
                                help("math")
                            elif x == 8:
                                help("statistics")
                    elif x == 6:
                        print("Vol. I - Batch")
                        print("Vol. II - Pip Package Installing")
                        print("Vol. III - Pip Package")
                        print("Vol. IV - Pip Package Topic")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - Execution")
                            print("Vol. II - Documentation")
                            x = int(input())
                            if x == 1:
                                help("os.system")
                            elif x == 2:
                                print("Vol. I - Command List")
                                print("Vol. II - Specific Commands")
                                x = int(input())
                                if x == 1:
                                    system("help")
                                elif x == 2:
                                    x = int(input("Command: "))
                                    system(f"help {x}")
                        elif x == 2:
                            help("pip")
                        elif x == 3:
                            print("Vol. I - Requests")
                            print("Vol. II - Rich")
                            print("Vol. III - Tqdm")
                            print("Vol. IV - Numpy")
                            print("Vol. V - Matplotlib")
                            print("Vol. VI - Shutil")
                            print("Vol. VII - Hashlib")
                            print("Vol. VIII - Textual")
                            print("Vol. IX - Urwid")
                            x = int(input())
                            if x == 1:
                                help("requests")
                            elif x == 2:
                                help("rich")
                            elif x == 3:
                                help("statements")
                            elif x == 4:
                                help("numpy")
                            elif x == 5:
                                help("matplotlib")
                            elif x == 6:
                                help("shutil")
                            elif x == 7:
                                help("hashlib")
                            elif x == 8:
                                help("textual")
                            elif x == 9:
                                help("urwid")
                        elif x == 4:
                            help("PACKAGES")
                    elif x == 7:
                        print("Vol. I - Documentation Access")
                        print("Vol. II - Syntax")
                        x = int(input())
                        if x == 1:
                            help()
                        elif x == 2:
                            print("Vol. I - Modules")
                            print("Vol. II - Key Words")
                            print("Vol. III - Symbols")
                            print("Vol. IV - Topics")
                    elif x == 8:
                        help("this")
                    elif x == 9:
                        print("Vol. I - Python")
                        print("Vol. II - Batch")
                        print("Vol. III - Any code")
                        x = int(input())
                        if x == 1:
                            print("Vol. I - Python Execution")
                            print("Vol. II - Python Evaluation")
                            x = int(input())
                            if x == 1:
                                help("exec")
                            elif x == 2:
                                help("eval")
                        elif x == 2:
                            help("os.system")
                        elif x == 3:
                            help("subprocess.run")
                    elif x == 10:
                        print("Vol. I - Opening Files")
                        print("Vol. II - File Opening Statement")
                        x = int(input())
                        if x == 1:
                            help("open")
                        elif x == 2:
                            help("with")
                elif x == 3:
                    print("1 to open Python shell")
                    print("2 to open Batch shell")
                    x = int(input("\n"))
                    if x == 1:
                        print("1 to open normal shell")
                        print("2 to open cool shell")
                        x = int(input("\n"))
                        if x == 1:
                            print("1 to open shell that doesn't recognize empty commands as unique syntax")
                            print("2 to open shell with opposite of option 1")
                            x = int(input("\n"))
                            if x == 1:
                                while True:
                                    x = input(">>> ")
                                    help(x)
                            elif x == 2:
                                while True:
                                    x = input(">>> ")
                                    if x == "":
                                        help()
                                    else:
                                        help(x)
                        elif x == 2:
                            help()
                    elif x == 2:
                        while True:
                            x = input(">>> ")
                            system(f"help {x}")
                elif x == 4:
                    print("1 to search in modules")
                    print("2 to search in keywords")
                    print("3 to search in symbols")
                    print("4 to search in topics")
                    x = int(input("\n"))
                    word = input("Word to search: ")
                    if x == 1:
                        help(f"modules {word}")
                    elif x == 2:
                        help(f"keywords {word}")
                    elif x == 2:
                        help(f"symbols {word}")
                    elif x == 2:
                        help(f"topics {word}")
                elif x == 5:
                    print("1 to get list of code stuff")
                    print("2 to get random documentation")
                    print("3 to get documentation of the day")
                    x = int(input("\n"))
                    if x == 1:
                        print("1 to open for Python")
                        print("2 to open for Batch")
                        x = int(input("\n"))
                        if x == 1:
                            for i in docs:
                                print(i)
                            print(docs)
                        elif x == 2:
                            for i in batch:
                                print(i)
                            print(batch)
                    elif x == 2:
                        print("1 to open for Python")
                        print("2 to open for Batch")
                        print("3 to open for all")
                        x = int(input("\n"))
                        print("Now, a random documentation will be opened.")
                        print("Maybe, you could create a project from this!")
                        if x == 1:
                            help(choice(docs))
                        elif x == 2:
                            system(f"help {choice(batch)}")
                        elif x == 3:
                            if randint(1, len(docs) + len(batch)) <= len(docs):
                                help(choice(docs))
                            else:
                                system(f"help {choice(batch)}")
                    elif x == 3:
                        print("1 to open for Python")
                        print("2 to open for Batch")
                        x = int(input("\n"))
                        if x == 1:
                            help(docs[datetime.now().year * datetime.now().month * datetime.now().day * datetime.now().hour * datetime.now().minute * datetime.now().second % len(docs)])
                        elif x == 2:
                            help(batch[datetime.now().year * datetime.now().month * datetime.now().day * datetime.now().hour * datetime.now().minute * datetime.now().second % len(batch)])
            elif x == 2:
                web("https://docs.python.org/")
        elif x == 3:
            try:
                run(["python", "code.py"], check=True)
            except CalledProcessError as e:
                print("The code shell was manually closed due to an unexpected error.")
        elif x == 4:
            print("TUI: Froggy_OS")
            print(f"OS: {name.title()}")
            print(f"Platform: {platform.title()}")
            print(f"Current Working Directory: {getcwd()}")
            print(f"User: {getcwd().split("\\")[2]}")
            system("systeminfo")
        elif x == 5:
            print("1 to change the current working directory")
            print("2 to create new directory")
            print("3 to list files in a directory")
            print("4 to delete files in a directory")
            print("5 to rename a file")
            print("6 to check if a file exists")
            print("7 to get size of a file")
            print("8 to write to a file")
            print("9 to read a file")
            print("10 to open a program")
            print("11 to ping an I.P. address")
            print("12 to edit source code")
            x = int(input("\n"))
            if x == 1:
                x = input(
                    "Please say something to change the current working directory.\n(e.g. \"../\".\nThe usual \"os.chdir()\" method.")
                chdir(x)
            elif x == 2:
                x = input("Parent directory: ")
                y = input("New directory name: ")
                mkdir(pathos.join(x, y))
            elif x == 3:
                x = input("Directory name: ")
                for i in listdir(x):
                    print(i)
            elif x == 4:
                x = input("Directory name: ")
                remove(x)
            elif x == 5:
                x = input("File name: ")
                y = input("Rename to what? ")
                rename(x, y)
            elif x == 6:
                x = input("File name: ")
                if pathos.exists(x):
                    print("This file exists.")
                else:
                    print("This file doesn't exist.")
            elif x == 7:
                x = input("File name: ")
                print(f"That file is {pathos.getsize(x)} bytes.")
            elif x == 8:
                print("1 to write entirely to a file")
                print("2 to append text to a file")
                x = int(input("\n"))
                if x == 1:
                    x = input("File name: ")
                    f = open(x, "w")
                elif x == 2:
                    x = input("File name: ")
                    f = open(x, "w")
                y = input("Write what? ")
                f.write(y)
                f.close()
            elif x == 9:
                x = input("File name: ")
                f = open(x, "r")
                print(f.read())
                f.close()
            elif x == 10:
                x = input("Program name: ")
                call(x)
            elif x == 11:
                x = input("I.P. address: ")
                p = Popen(f"ping {x}", stdout=SPPIPE)
                if p.poll():
                    print("I.P. address active")
                else:
                    print("I.P. address passive")
            elif x == 12:
                input("You can run Python and Batch code here.\nBut the variables, lists, dicts e.t.c. are the ones from the code of the actual OS code.\n")
                print("1 to run Python code")
                print("2 to run Batch code")
                x = int(input("\n"))
                if x == 1:
                    print("1 to execute Python code")
                    print("2 to evaluate Python code")
                    x = int(input("\n"))
                    if x == 1:
                        shell()
                        try:
                            exec(">>> ")
                        except Exception as e:
                            if e != None:
                                print(e)
                    elif x == 2:
                        shell()
                        try:
                            print(eval(input(">>> ")))
                        except Exception as e:
                            if e != None:
                                print(e)
                elif x == 2:
                    shell()
                    try:
                        system(">>> ")
                    except Exception as e:
                        if e != None:
                            print(e)
        elif x == 6:
            f = open("readme.txt", "r")
            print(f.read())
            f.close()
        elif x == 7:
            print("1 to import and get syntax list of a normal Python module")
            print("2 to import and get syntax list of a normal Pip library Batch module")
            print("3 to uninstall and get syntax list of a normal Pip library Batch module")
            x = int(input("\n"))
            if x == 1:
                x = input("Get syntax list of which module? ")
                m = __import__(x)
                print(dir(m))
            elif x == 2:
                x = input("Get syntax list of which module? ")
                system(f"pip install {x}")
                print(dir(x))
            elif x == 3:
                x = input("Get syntax list of which module? ")
                system(f"pip install {x}")
                print(dir(x))
                system(f"pip uninstall {x}")
        elif x == 8:
            print("1 to open Batch")
            print("2 to open PowerShell")
            print("2 to open general Python shell")
            print("3 to open gPs for evaluation")
            print("4 to open WMI information shell")
            x = int(input("\n"))
            if x == 1:
                x = int(input("Run how many commands? "))
                shell()
                for i in range(x):
                    try:
                        system(input("$ "))
                    except Exception as e:
                        if e != None:
                            print(e)
            elif x == 2:
                system("cmd")
            elif x == 3:
                x = int(input("Run how many commands? "))
                shell()
                for i in range(x):
                    try:
                        exec(input(">>> "))
                    except Exception as e:
                        if e != None:
                            print(e)
            elif x == 4:
                x = int(input("Run how many commands? "))
                shell()
                for i in range(x):
                    try:
                        print(eval(input(">>> ")))
                    except Exception as e:
                        if e != None:
                            print(e)
            elif x == 5:
                system("wmic")
        elif x == 9:
            list = eval(input("Enter list to sort as a Python list (e.g. \"[1, 2, 3]\"): "))
            print(list, type(list))
            args = []
            agam = list.copy()
            agam.sort()
            print("1 for Stalin Sort (for int, float)")
            print("2 for Sleep Sort (for int)")
            print("3 for Bogo Sort (for int, float, str, bool)")
            print("4 for Bozo Sort (for int, float)")
            print("5 for Quantum Bogo Sort (for int, float, str, bool)")
            print("6 for Schrodinger's Sort (for int, float, str, bool)")
            print("7 for Intelligent Design Sort (for int, float, str, bool)")
            print("8 for Miracle Sort (for int, float, str, bool)")
            print("9 for Quick Sort (for int, float, str, bool)")
            x = int(input("\n"))
            if x == 1:
                print(list)
                print(args)
                for i in range(len(list)):
                    try:
                        if list[i] >= list[i - 1]:
                            args.append(i)
                        print(args)
                    except IndexError:
                        print(args)
                print(args)
            elif x == 2:
                print(list)
                print(args)
                x = 0
                while not(args == agam):
                    for i in agam:
                        if i == x:
                            args.append(x)
                            print(args)
                    sleep(1)
                    x += 1
                print(args)
            elif x == 3:
                print(list)
                while not(list == agam):
                    shuffle(list)
                    print(list)
            elif x == 4:
                print(list)
                while not(list == args):
                    x = randint(0, len(list) - 1)
                    y = randint(0, len(list) - 1)
                    if x > y and list[x] < list[y]:
                        a = list[x]
                        b = list[y]
                        list[x] = b
                        list[y] = a
                        print(list)
                    if x > y and list[x] < list[y]:
                        a = list[x]
                        b = list[y]
                        list[x] = b
                        list[y] = a
                        print(list)
                print(list)
            elif x == 5:
                print(list)
                args = list.copy()
                while not(args == agam):
                    shuffle(args)
                    print(args)
            elif x == 6:
                print(f"½ chance to be {list}")
                print(f"½ chance to be {agam}")
                print(f"List is unknown")
            elif x == 7:
                print(f"1/(n!) chance for list ({list}) to be sorted")
            elif x == 8:
                print("Eventually, a miracle will happen and the list will be sorted.")
                print(list)
            elif x == 9:
                print(agam)
        elif x == 10:
            print("The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!")
        elif x == 11:
            print("1 to select text to print manually")
            print("2 to select text to print from files")
            x = int(input("\n"))
            if x == 1:
                x = input("Enter text: ")
            elif x == 2:
                x = input("Enter text's file: ")
                x = open(x, "r")
                x = x.read()
            y = float(input("Time between each printing (as seconds): "))
            letter = 0
            nw = []
            while not (nw == x):
                try:
                    nw.append(" ")
                    while not (nw[-1] == x[letter]):
                        nw[-1] = chr(ord(nw[-1]) + 1)
                        for i in nw:
                            print(i, end="")
                        print("")
                        sleep(y)
                    letter += 1
                except IndexError:
                    nw = x
        elif x == 12:
            print("1 to manage Python modules")
            print("2 to manage Pip packages")
            x = int(input("\n"))
            if x == 1:
                print("1 to import a Python module with \"import ...\"")
                print("2 to import a Python module with \"from ... import ...\"")
                x = int(input("\n"))
                if x == 1:
                    n1 = input("Import which module? (import OOO as ooo) ")
                    n2 = input("Import module as what name? (import ooo as OOO) ")
                    exec(f"import {n1} as {n2}")
                elif x == 2:
                    n1 = input("Import which module? (from OOO import ooo as ooo) ")
                    n2 = input("Import which functions from the module? (from ooo import OOO as ooo) ")
                    n3 = input("Import module as what name? (from ooo import ooo as OOO) ")
                    exec(f"from {n1} import {n2} as {n3}")
            elif x == 3:
                print("1 to install Pip package")
                print("2 to uninstall Pip package")
                x = int(input("\n"))
                if x == 1:
                    n1 = input("Install which Pip package? (pip install OOO) ")
                    system(f"pip install {n1}")
                elif x == 1:
                    n1 = input("Uninstall which Pip package? (pip uninstall OOO) ")
                    system(f"pip uninstall {n1}")
        elif x == 13:
            print("1. George Boole")
            print("Created Boolean logic (0 and 1, False and True, off and on e.t.c.), the basics for computer.")
            print("2. Countess Ada Lovelace")
            print("Math enthusiast, also created the first basic programming language, and close friend of Charles Babbage.")
            print("3. Charles Babbage")
            print("Mathematician and philosopher, made a concept of a digital computer that can be programmed.")
            print("4. Monty Python")
            print("A BBC-show's main character titled \"Monty Python's Flying Circus\" that Guido van Rossum likes.")
            print("5. Guido van Rossum")
            print("Dutch (as said on the Zen of Python) programmer that made Python programming language that got inspired from MPFC.")
            print("6. Tim Peters")
            print("Python programmer that improved the language, and wrote the Zen of Python that teached how to write \"pythonic\" code.")
            print("7. Urban Müller")
            print("Programmer who created the smallest programming language that I call +-<>.,[] as a successor to FALSE.")
            print("8. David Morgan-Mar")
            print("Biggest esoteric programming language developer that made esolangs like image-based Piet, recipe-based Chef, random time-based Whenever and OOP-based ZOMBIE.")
            print("9. Markus Persson")
            print("Game developer who made games like 0x10c, RubyDung, the Legend of the Chambered and Cave Game which got given to Mojang as Minecraft.")
            print("10. Mojang Studios Team")
            print("A game studio that made games like Minecraft, Cobalt, Caller's Bane (Scrolls) that include Nathan Adams, Jens Bergensten, Agnes Larsson e.t.c..")
            print("11. Shigeru Miyamoto")
            print("1980's console game developer working on Nintendo that made small games like Super Mario Bros., the Legend of Zelda and Devil World.")
            print("12. Bill Gates")
            print("Leader of MicroSoft, known mainly by building Windows OS, and video games made for XBox game console system.")
            print("13. Steve Jobs")
            print("Founder of Apple Computer Inc. which made computers like Apple ][, also programming languages like Objective-C and Swift.")
            print("14. Linus Torwalds")
            print("Founder of Linux, a sub-program for GNU with a lot of distributions where code can do anything you want which is both open-source, lightweight and fast.")
            print("14. Terry Davis")
            print("Schizophrenic prophet that's chosen by god to make his 3rd temple as a ring-0 operating system, TempleOS (LoseThos).")
            print("15. Alan Turing")
            print("Created the Turing Machine, a machine that can calculate anything that can be simulated with a programming language with 8 characters: \"+-<>.,[]\"")
            print("16. John von Neumann")
            print("Made a cellular automata with 29 states for cells, much more complicated than Conway's Game of Life which is also the predecessor of it.")
            print("17. John Conway")
            print("Made a Turing-complete cellular automata on a 2D grid with only 3 rules and 2 states that's so simple, that it's complicated and called \"Conway's Game of Life\".")
        elif x == 14:
            while True:
                input()
    elif x == 4:
        print("1 to manage cases")
        print("2 to strip letters")
        print("3 to learn length")
        print("4 to manage words in words")
        print("5 to change letters")
        print("6 to find letters/numbers")
        x = int(input("\n"))
        if x == 1:
            x = input("Enter text: ")
            print(f"Uppercase text: {edit(x, "upper")}")
            print(f"Lowercase text: {edit(x, "lower")}")
            print(f"Cases Swapped text: {edit(x, "swapcase")}")
            print(f"Capitalized text: {edit(x, "capitalize")}")
            print(f"Titled text: {edit(x, "title")}")
        elif x == 2:
            print("1 to strip from all sides")
            print("2 to strip from left")
            print("3 to strip from right")
            x = int(input("\n"))
            y = input("Enter word: ")
            z = input("Enter what will be stripped: ")
            print(f"y.{dict[x]}(z)")
        elif x == 3:
            x = input("Enter word: ")
            print(f"Length: {len(x)}")
        elif x == 4:
            print("1 to check if a word is in a word")
            print("2 to count the number of a word in a word")
            print("3 to locate a letter in a word")
            x = int(input("\n"))
            if x == 1:
                x = input("The word you're searching for: ")
                y = input("The word you're searching that word in: ")
                if x in y:
                    print("There's that word in that word.")
                else:
                    print("There isn't that word in that word.")
            elif x == 2:
                x = input("The word you're counting: ")
                y = input("The word you're counting that word in: ")
                print(f"There's {y.count(x)} words in that word.")
            elif x == 3:
                x = input("The letter you're locating: ")
                y = input("The word you're counting that word in: ")
                print(f"The letter's position in that word is the {y.index(x)}. letter.")
        elif x == 5:
            x = input("Enter word to change letter in: ")
            y = int(input("Which letter of the word will you change? "))
            z = input("Change to what?")
            list = []
            for i in range(len(x)):
                list.append(x[i])
            list[y] = z
            p = ""
            for i in x:
                p = f"{p}{i}"
            print(f"New word:\n{p}")
        elif x == 6:
            x = input("Enter word: ")
            if x.isalnum():
                print("That word has both letters and numbers.")
            elif x.isalpha():
                print("That word has letters.")
            elif x.isnumeric():
                print("That word has numbers.")
            if x.isalnum() or x.isalpha():
                if x.isupper():
                    print("That word is uppercase.")
                elif x.islower():
                    print("That word is lowercase.")
    elif x == 5:
        if firsttime:
            print(
                "To access internet, please make sure that you have a computer (preferably Windows) that hasn't ended support. ")
            print("And connect to a WiFi network. ")
            print(
                "Finally, make sure that you have Microsoft Edge or Internet Explorer (or Google Chrome) and make it your default browser. ")
            print("Also, make your default search engine Microsoft Bing (or Google!). ")
            firsttime = False
        else:
            print("1 to open a website")
            print("2 to open bookmarks")
            print("3 to open featured websites")
            x = int(input("\n"))
            if x == 1:
                print("1 to search something")
                print("2 to open a website")
                print("3 to open new tab")
                x = int(input("\n"))
                if x == 1:
                    print("1 to search on Microsoft Bing")
                    print("2 to search on Google!")
                    print("3 to search on Yandex")
                    print("4 to search on DuckDuckGo")
                    print("5 to search on Yahoo!")
                    print("6 to search on YouTube")
                    print("7 to search on Twitch")
                    print("8 to search on Vine")
                    print("9 to search on Ask.com")
                    print("10 to search on Ask Jeeves!")
                    x = int(input("\n"))
                    if x == 1:
                        x = input("What to search? ")
                        web(f"https://www.bing.com/search?q={x}")
                    elif x == 2:
                        x = input("What to search? ")
                        web(f"https://www.google.com/search?q={x}")
                    elif x == 3:
                        x = input("What to search? ")
                        web(f"https://yandex.com/search/?text={x}")
                    elif x == 4:
                        x = input("What to search? ")
                        web(f"https://duckduckgo.com/?t=h_&q={x}")
                    elif x == 5:
                        x = input("What to search? ")
                        web(f"https://search.yahoo.com/search?p={x}")
                    elif x == 6:
                        x = input("What to search? ")
                        web(f"https://youtube.com/results?search_query={x}")
                    elif x == 7:
                        x = input("What to search? ")
                        web(f"https://www.twitch.tv/search?term={x}")
                    elif x == 8:
                        x = input("What to search? ")
                        web(f"https://vine.co/search?q={x}")
                    elif x == 9:
                        x = input("What to search? ")
                        web(f"https://www.ask.com/web?q={x}")
                    elif x == 10:
                        x = input("What to search? ")
                        web(f"https://www.askjeeves.com/web?q={x}")
                elif x == 2:
                    print("1 to enter URL")
                    print("2 to enter its name (when you forgot the URL)")
                    x = int(input("\n"))
                    if x == 1:
                        x = input("URL: ")
                        web(x)
                    elif x == 2:
                        x = input("Name (e.g. \"python\"): ")
                        input("We will now try to find a website with that name.\n")
                        y = input("Open suspicious websites (y/n)? ")
                        x = x.lower()
                        web(f"https://www.{x}.com")
                        web(f"https://www.{x}.org")
                        web(f"https://www.{x}.gov")
                        web(f"https://www.{x}.net")
                        web(f"https://www.{x}.edu")
                        web(f"https://www.{x}.co.uk")
                        web(f"https://www.{x}.ru")
                        if "y" in y.lower():
                            web(f"https://www.{x}.io")
                            web(f"https://www.{x}.xyz")
                            web(f"https://www.{x}.fun")
                            web(f"https://www.{x}.website")
                            web(f"https://www.{x}.tv")
                elif x == 3:
                    x = input("URL: ")
                    open_new_tab(x)
            elif x == 2:
                print("1 to open bookmark websites")
                print("2 to edit bookmarks")
                print("3 to list bookmarks")
                x = int(input("\n"))
                if x == 1:
                    for i in range(len(bmn)):
                        print(f"{i + 1} to open {bmn[i]}")
                    x = int(input("\n"))
                    print(f"Opening {bm[x - 1]}")
                    web(bm[x - 1])
                elif x == 2:
                    print("1 to edit bookmark names")
                    print("2 to edit bookmark URL's")
                    x = int(input("\n"))
                    if x == 1:
                        for i in range(len(bmn)):
                            print(f"{i} to edit {bmn[i]}")
                            x = int(input("\n"))
                        y = int(input("New bookmark name: "))
                        bmn[x] = y
                    elif x == 2:
                        for i in range(len(bm)):
                            print(f"{i} to edit {bm[i]}")
                        x = int(input("\n"))
                        y = int(input("New bookmark URL: "))
                        bm[x] = y
                elif x == 3:
                    for i in range(len(bmn)):
                        print(f"{i}. {bmn[i]} ({bm[i]})")
            elif x == 3:
                for i in url:
                    print(i)
