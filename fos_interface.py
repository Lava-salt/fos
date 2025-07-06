# head (module importing)

from os import system, getcwd
from sys import platform
from subprocess import run
from random import randint
from codecs import encode
from tkinter.constants import FALSE  # i didn't import this, how is this even here and what is it used for

# head (other variables' defining)

global pointer
pointer = 0
def goto(n):
    global pointer
    pointer = n
code = []
def bf(code, input_data):
    memory = []
    for i in range(256):
        memory.append(0)
    pointer = 0
    code_pointer = 0
    input_pointer = 0
    output = []
    loop_stack = []
    stack = []
    while code_pointer < len(code):
        command = code[code_pointer]
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output.append(chr(memory[pointer]))
        elif command == ',':
            if input_pointer < len(input_data):
                memory[pointer] = ord(input_data[input_pointer])
                input_pointer += 1
            else:
                memory[pointer] = 0
        elif command == ';':
            output.append(memory[pointer])
        elif command == '#':
            memory[pointer] = 0
        elif command == '@':
            if pointer < len(memory) - 1:
                memory[pointer + 1] = memory[pointer]
        elif command == '&':
            if pointer > 0:
                memory[pointer], memory[pointer - 1] = memory[pointer - 1], memory[pointer]
        elif command == '%':
            memory[pointer] = (memory[pointer] * 2) % 256
        elif command == '$':
            memory[pointer] = memory[pointer] // 2
        elif command == '^':
            while pointer > 0 and memory[pointer] == 0:
                pointer -= 1
        elif command == '~':
            while pointer < len(memory) - 1 and memory[pointer] != 0:
                pointer += 1
        elif command == '(':
            stack.append(memory[pointer])
        elif command == ')':
            if stack:
                memory[pointer] = stack.pop()
        elif command == '[':
            if memory[pointer] == 0:
                open_loops = 1
                while open_loops > 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_loops += 1
                    elif code[code_pointer] == ']':
                        open_loops -= 1
        elif command == ']':
            if memory[pointer] != 0:
                close_loops = 1
                while close_loops > 0:
                    code_pointer -= 1
                    if code[code_pointer] == ']':
                        close_loops += 1
                    elif code[code_pointer] == '[':
                        close_loops -= 1
        code_pointer += 1
    for i in output:
        print(i, end="")
def shell():
    print(
        f'Python 3.8.5 (default, Jul 20 2020, 23:11:29) [GCC 9.3.0] on {platform}\nType "help", "copyright", "credits" or "license" for more information.')
def hq(y):
    list = []
    for i in range(len(y)):
        list.append(y[i])
    num = 0
    list1 = 0
    stack = []
    for x in list:
        if x == "C":
            print(input())
        elif x == "H":
            print("Hello, World!")
        elif x == "I":
            hq(input())
        elif x == "Q":
            print(y)
        elif x == "R":
            print(encode(input(), "rot_13"))
        elif x == "S":
            l1 = []
            for i in range(randint(1, 10)):
                l1.append(input())
            l1.sort()
            print(l1)
        elif x == "9":
            for i in range(99, 0, -1):
                print(f"{i} bottles of beer on the wall!")
                print(f"{i} bottles of beer!")
                print("Take one down, pass it around")
                print(f"{i - 1} bottles of beer on the wall!")
        elif x == "+":
            num += 1
        elif x == "-":
            try:
                if list[list1 - 1] == "F":
                    print(None.split(" "))
                else:
                    num -= 1
            except IndexError:
                num -= 1
        elif x == "*":
            num *= 2
        elif x == "/":
            num /= 3
        elif x == "%":
            num %= 2
        elif x == "x":
            num **= 2
        elif x == "X":
            num **= 3
        elif x == "&":
            num //= 3
        elif x == "A":
            print(num)
        elif x == "F":
            for i in range(101):
                if i % 3 == 0 and i % 5 == 0:
                    print(f"FizzBuzz ({i})")
                elif i % 3 == 0:
                    print(f"Fizz ({i})")
                elif i % 5 == 0:
                    print(f"Buzz ({i})")
                else:
                    print(i)
        elif x == "$":
            stack.append(num)
        elif x == "#":
            p = stack[-1]
            del stack[-1]
            print(p, end="")
        elif x == "^":
            p = stack[-1]
            del stack[-1]
            print(chr(p), end="")
        elif x == "=":
            print()
        elif x == "/":
            num = int(input())
        elif x == "\\":
            num = ord(input())
        elif x == "P":
            stack.append(input())
        elif x == ">":
            p = stack[-1]
            del stack[-1]
            exec(p)
        elif x == "<":
            p = stack[-1]
            del stack[-1]
            print(eval(p))
        elif x == "½":
            p = stack[-1]
            del stack[-1]
            system(p)
        elif x == "0":
            num = bin(num)
        elif x == "2":
            t = [2, 3]
            for i in t:
                for j in t:
                    print(f"{i} x {j} = {i * j}")
            for i in t:
                for j in t:
                    for k in t:
                        print(f"{i} x {j} x {k} = {i * j * k}")
            for i in t:
                for j in t:
                    for k in t:
                        for l in t:
                            print(f"{i} x {j} x {k} x {l} = {i * j * k * l}")
            for i in t:
                for j in t:
                    for k in t:
                        for l in t:
                            for m in t:
                                print(f"{i} x {j} x {k} x {l} x {m} = {i * j * k * l * m}")
        elif x == "G":
            print("Hello World, I'm Gay!")
        elif x == ":":
            stack.append(chr(num))
        elif x == ";":
            stack[-1] = stack[-1] + chr(num)
        list1 += 1
        """elif x == "@":
                    hq(y[list1 : len(y) + 1])
                elif x == "€":
                    for i in range(2):
                        hq(y[list1 : len(y) + 1])
                elif x == "é":
                    while True:
                        hq(y[list1 : len(y) + 1])"""
def df(code):
    st = False
    stn = "t"
    stf = "iiiiiiiiii"
    x = 0
    for j in range(len(code)):
        i = code[j]
        if st:
            stn, stf = "", ""
            if code[j - 1] == "H" or i == " ":
                pass
            elif i == "H":
                stn = code[j + 1]
            elif i == "S":
                st = False
            else:
                stf = stf + i
        else:
            if i == stn:
                df(stf)
            elif i == "i":
                x += 1
            elif i == "d":
                x -= 1
            elif i == "s":
                x *= x
            elif i == "o":
                print(x)
            elif i == "ö":
                print(x, end="")
            elif i == "h":
                return 1
            elif i == "I":
                st = True
            elif i == "D":
                x = 0
            elif i == "O":
                print(chr(x))
            elif i == "Ö":
                print(chr(x), end="")
            elif i == "x":
                quit()
            elif i == "?":
                print(stn)
            elif i == "!":
                print(stf)
            else:
                pass
    return 0

# body (code)

print("1 to run Python code")
print("2 to run Batch code")
print("3 to run Brainf**k code")
print("4 to run any code")
print("5 to open documentation shell")
print("6 to open esoteric programming languages")
x = int(input("\n"))
if x == 1:
    print("1 to execute Python code")
    print("2 to evaluate Python code")
    print("3 to open general shell")
    x = int(input("\n"))
    if x == 1:
        print("1 to run enhanced version")
        print("2 to execute single-line commands")
        print("3 to execute from files")
        print("4 to open debugger")
        x = int(input("\n"))
        if x == 1:
            print("1 to get information")
            print("2 to really execute")
            print("3 to execute from files")
            x = int(input("\n"))
            if x == 1:
                print("You can run enhanced Python programs, like running AppleSoft BASIC in Apple ][. ")
                print("Write normal syntax, but start with a number that's the line number of the code line. ")
                print("For example, like \"10 print('executed on line 10')\". There's also some extra functions. ")
                print("\"goto(int)\" is used for making the executing line change to the given integer. ")
                print("For example, \"10 x = 0 20 print(x) 30 x += 1 40 goto 2\" code counts forever. ")
                print(
                    "\"listcode\" command lists the entire code, and \"run\" runs the code in the lines from smallest to biggest. ")
                print("Use the \"bf(code, input_data)\" function to execute Brainf**k code. ")
                print("Use the \"hq(code)\" function to execute HQ9+ code (but with 31 commands!) and \"df(code)\" to execute DeadFish (with more commands).")
                print("Use \"new\" syntax to clean your code.")
                print("You can have a save code for your code and load it with \"save\" and \"load\" keywords. ")
                print(
                    "You can execute files. For example, writing \"python3 file.txt\" will execute \"file.txt\" in Python 3.")
                print("You can also do other things like \"python3 -c print(\"hi\")\" to print \"hi\".")
                print(
                    "DO NOT use the \"kur\", \"gawk\", \"code\" and \"pointer\" as variables, lists, tuples, dicts e.t.c. as this could break the code. ")
                print("Sorry but these are highly necessary for the code to run. ")
                input("Example program: ")
                print("10 print('Number Sum Finder')")
                print("20 x = input('Number 1: ')")
                print("30 y = input('Number 2: ')")
                print("31 x = int(x)")
                print("32 y = int(y)")
                print("40 print(f'The sum of {x} and {y} is {x+y}')")
                print("45 z = 0")
                print("50 z = input('Want to do it again? (y/n)')")
                print("60 goto(0) if 'y' in z.lower()")
                print("# now i'll list the project code for debug:")
                print("listcode")
                input("run ")
            elif x == 2:
                shell()
                del x
                while True:
                    kur = []
                    for i in code:
                        kur.append(i)
                    for i in range(len(kur)):
                        tul = kur[i]
                        pul = tul.split()
                        kur[i] = int(pul[0])
                    code.append(input("> "))
                    pul = code[-1].split()
                    if pul[0].isnumeric():
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        print("", end="")
                    else:
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        if code[-1] == "run":
                            del code[-1]
                            pointer = 0
                            pagot = int(input("Run how many lines? "))
                            shell()
                            while pointer < pagot:
                                pointer += 1
                                for i in code:
                                    gawk = i.split()
                                    del gawk[0]
                                    gawk = " ".join(gawk)
                                    if eval(i.split()[0]) == pointer:
                                        try:
                                            exec(gawk)
                                        except Exception as e:
                                            if e != None:
                                                print(e)
                        elif code[-1] == "listcode":
                            del code[-1]
                            for i in code:
                                print(i)
                        elif code[-1] == "save":
                            del code[-1]
                            print(code)
                        elif code[-1] == "load":
                            del code[-1]
                            code = eval(input("Save code >>> "))
                        elif code[-1] == "new":
                            del code[-1]
                            code = []
                        else:
                            try:
                                run(code[-1].split(" "))
                            except Exception:
                                try:
                                    exec(code[-1])
                                except Exception as e:
                                    if e != None:
                                        print(e)
                            del code[-1]
            elif x == 3:
                print("Please go to the \"really execute\" option and get a save code of your project.")
                x = input("And copy it, then paste it to a file. Are you ready? (y/n) ")
                if "y" in x.lower():
                    del x
                    kur = []
                    for i in code:
                        kur.append(i)
                    for i in range(len(kur)):
                        tul = kur[i]
                        pul = tul.split()
                        kur[i] = int(pul[0])
                    code.append("load")
                    pul = code[-1].split()
                    if pul[0].isnumeric():
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        print("", end="")
                    else:
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        if code[-1] == "run":
                            del code[-1]
                            pointer = 0
                            pagot = int(input("Run how many lines? "))
                            shell()
                            while pointer < pagot:
                                pointer += 1
                                for i in code:
                                    gawk = i.split()
                                    del gawk[0]
                                    gawk = " ".join(gawk)
                                    if eval(i.split()[0]) == pointer:
                                        try:
                                            exec(gawk)
                                        except Exception as e:
                                            if e != None:
                                                print(e)
                        elif code[-1] == "listcode":
                            del code[-1]
                            for i in code:
                                print(i)
                        elif code[-1] == "save":
                            del code[-1]
                            print(code)
                        elif code[-1] == "load":
                            del code[-1]
                            f = open(input("Save code's file >>> "), "r")
                            p = f.read()
                            code = eval(p)
                            f.close()
                        elif code[-1] == "new":
                            del code[-1]
                            code = []
                        else:
                            try:
                                exec(code[-1])
                            except Exception as e:
                                if e != None:
                                    print(e)
                            del code[-1]
                    del f, p
                    kur = []
                    for i in code:
                        kur.append(i)
                    for i in range(len(kur)):
                        tul = kur[i]
                        pul = tul.split()
                        kur[i] = int(pul[0])
                    code.append("run")
                    pul = code[-1].split()
                    if pul[0].isnumeric():
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        print("", end="")
                    else:
                        try:
                            del pul
                        except NameError:
                            print("", end="")
                        try:
                            del tul
                        except NameError:
                            print("", end="")
                        if code[-1] == "run":
                            del code[-1]
                            pointer = 0
                            pagot = int(input("Run how many lines? "))
                            shell()
                            while pointer < pagot:
                                pointer += 1
                                for i in code:
                                    gawk = i.split()
                                    del gawk[0]
                                    gawk = " ".join(gawk)
                                    if eval(i.split()[0]) == pointer:
                                        try:
                                            exec(gawk)
                                        except Exception as e:
                                            if e != None:
                                                print(e)
                        elif code[-1] == "listcode":
                            del code[-1]
                            for i in code:
                                print(i)
                        elif code[-1] == "save":
                            del code[-1]
                            print(code)
                        elif code[-1] == "load":
                            del code[-1]
                            code = eval(input("Save code >>> "))
                        elif code[-1] == "new":
                            del code[-1]
                            code = []
                        else:
                            try:
                                exec(code[-1])
                            except Exception as e:
                                if e != None:
                                    print(e)
                            del code[-1]
        elif x == 2:
            print("1 to execute normally")
            print("2 to execute coolly")
            x = int(input("\n"))
            if x == 1:
                del x, code, pointer
                shell()
                while True:
                    try:
                        exec(input(">>> "))
                    except Exception as e:
                        if e != None:
                            print(e)
            elif x == 2:
                del x, code, pointer
                print(getcwd())
                print(
                    f"--mode=client --host={randint(100, 999)}.{randint(0, 9)}.{randint(0, 9)}.{randint(0, 9)} --port={randint(10000, 99999)}")
                print("import sys; print('Python %s on %s' % (sys.version, sys.platform))")
                print(f"sys.path.extend(['{getcwd()}'])")
                print("PyDev console: starting.")
                print(f"Python 3.8.5 (tags/v3.8.5, Jul 20 2020, 23:11:29) [MSC v.1941 64 bit (AMD64)] on {platform}")
                shell()
                while True:
                    try:
                        exec(input(">>> "))
                    except Exception as e:
                        if e != None:
                            print(e)
        elif x == 3:
            del x, code, pointer
            f = open(input("File name: "), "r")
            try:
                exec(f.read())
            except Exception as e:
                if e != None:
                    print(e)
            f.close()
        elif x == 4:
            del code, pointer
            print("1 to debug manually")
            print("2 to debug from files")
            x = int(input("\n"))
            if x == 1:
                print("1 to debug 1 line of code")
                print("2 to debug multiple lines")
                x = int(input("\n"))
                if x == 1:
                    x = input("Enter Python code.\n")
                    try:
                        exec(x)
                        print("Code execution successful: Return code 0")
                    except Exception as e:
                        print("Code execution failed: Return code 1")
                        print("Exception (error) type: ")
                        print(e)
                elif x == 2:
                    x = input("Enter Python code's file.\n")
                    f = open(x, "r")
                    x = f.read()
                    f.close()
                    try:
                        exec(x)
                        print("Code execution successful: Return code 0")
                    except Exception as e:
                        print("Code execution failed: Return code 1")
                        print("Exception (error) type: ")
                        print(e)
            elif x == 2:
                print("1 to debug 1 line of code")
                print("2 to debug multiple lines")
                x = int(input("\n"))
                if x == 1:
                    x = input("Enter Python codes as a Python list.\n")
                    x = eval(x)
                    try:
                        for i in x:
                            exec(i)
                        print("Code execution successful: Exit code 0")
                    except Exception as e:
                        print("Code execution failed: Exit code 1")
                        print("Exception (error) type: ")
                        print(e)
                elif x == 2:
                    x = input("Enter Python codes as a Python list's file.\n")
                    f = open(x, "r")
                    x = eval(f.read())
                    f.close()
                    try:
                        for i in x:
                            exec(i)
                        print("Code execution successful: Exit code 0")
                    except Exception as e:
                        print("Code execution failed: Exit code 1")
                        print("Exception (error) type: ")
                        print(e)
    elif x == 2:
        print("1 to evaluate single-line commands")
        print("2 to evaluate from files")
        x = int(input("\n"))
        if x == 1:
            del x, code, pointer
            shell()
            while True:
                try:
                    print(eval(input(">>> ")))
                except Exception as e:
                    if e != None:
                        print(e)
        elif x == 2:
            del x, code, pointer
            f = open(input("File name: "), "r")
            try:
                print(eval(f.read()))
            except Exception as e:
                if e != None:
                    print(e)
            f.close()
    elif x == 3:
        help()
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
elif x == 2:
    print("1 to run enhanced version")
    print("2 to execute single-line commands")
    print("3 to execute from files")
    x = int(input("\n"))
    if x == 1:
        print("1 to really execute")
        print("2 to execute from files")
        x = int(input("\n"))
        if x == 1:
            print("You can run enhanced Batch programs, like running AppleSoft BASIC in Apple ][. ")
            print("Write normal syntax, but start with a number that's the line number of the code line. ")
            print("For example, like \"10 echo \"executed on line 10\"\". There's also some extra functions. ")
            print(
                "\"listcode\" command lists the entire code, and \"run\" runs the code in the lines from smallest to biggest. ")
            print("You can have a save code for your code and load it with \"save\" and \"load\" keywords. ")
            print("Use \"new\" syntax to clean your code.")
            print("You can have a save code for your code and load it with \"save\" and \"load\" keywords. ")
            print(
                "You can execute files. For example, writing \"python3 file.txt\" will execute \"file.txt\" in Python 3.")
            print("You can also do other things like \"python3 -c print(\"hi\")\" to print \"hi\".")
            print(
                "DO NOT use the \"kur\", \"gawk\", \"code\" and \"pointer\" as variables, lists, tuples, dicts e.t.c. as this could break the code. ")
            input("Sorry but these are highly necessary for the code to run. ")
            shell()
            del x
            while True:
                kur = []
                for i in code:
                    kur.append(i)
                for i in range(len(kur)):
                    tul = kur[i]
                    pul = tul.split()
                    kur[i] = int(pul[0])
                code.append(input("$ "))
                pul = code[-1].split()
                if pul[0].isnumeric():
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    print("", end="")
                else:
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    if code[-1] == "run":
                        del code[-1]
                        pointer = 0
                        pagot = int(input("Run how many lines? "))
                        shell()
                        while pointer < pagot:
                            pointer += 1
                            for i in code:
                                gawk = i.split()
                                del gawk[0]
                                gawk = " ".join(gawk)
                                if eval(i.split()[0]) == pointer:
                                    try:
                                        system(gawk)
                                    except Exception as e:
                                        if e != None:
                                            print(e)
                    elif code[-1] == "listcode":
                        del code[-1]
                        for i in code:
                            print(i)
                    elif code[-1] == "save":
                        del code[-1]
                        print(code)
                    elif code[-1] == "load":
                        del code[-1]
                        code = eval(input("Save code >>> "))
                    elif code[-1] == "new":
                        del code[-1]
                        code = []
                    else:
                        try:
                            run(code[-1].split(" "))
                        except Exception:
                            try:
                                system(code[-1])
                            except Exception as e:
                                if e != None:
                                    print(e)
                        del code[-1]
        elif x == 2:
            print("Please go to the \"really execute\" option and get a save code of your project.")
            x = input("And copy it, then paste it to a file. Are you ready? (y/n) ")
            if "y" in x.lower():
                del x
                kur = []
                for i in code:
                    kur.append(i)
                for i in range(len(kur)):
                    tul = kur[i]
                    pul = tul.split()
                    kur[i] = int(pul[0])
                code.append("load")
                pul = code[-1].split()
                if pul[0].isnumeric():
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    print("", end="")
                else:
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    if code[-1] == "run":
                        del code[-1]
                        pointer = 0
                        pagot = int(input("Run how many lines? "))
                        shell()
                        while pointer < pagot:
                            pointer += 1
                            for i in code:
                                gawk = i.split()
                                del gawk[0]
                                gawk = " ".join(gawk)
                                if eval(i.split()[0]) == pointer:
                                    try:
                                        system(gawk)
                                    except Exception as e:
                                        if e != None:
                                            print(e)
                    elif code[-1] == "listcode":
                        del code[-1]
                        for i in code:
                            print(i)
                    elif code[-1] == "save":
                        del code[-1]
                        print(code)
                    elif code[-1] == "load":
                        del code[-1]
                        f = open(input("Save code's file >>> "), "r")
                        p = f.read()
                        code = eval(p)
                        f.close()
                    elif code[-1] == "new":
                        del code[-1]
                        code = []
                    else:
                        try:
                            run(code[-1].split(" "))
                        except Exception:
                            try:
                                system(code[-1])
                            except Exception as e:
                                if e != None:
                                    print(e)
                        del code[-1]
                del f, p
                kur = []
                for i in code:
                    kur.append(i)
                for i in range(len(kur)):
                    tul = kur[i]
                    pul = tul.split()
                    kur[i] = int(pul[0])
                code.append("run")
                pul = code[-1].split()
                if pul[0].isnumeric():
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    print("", end="")
                else:
                    try:
                        del pul
                    except NameError:
                        print("", end="")
                    try:
                        del tul
                    except NameError:
                        print("", end="")
                    if code[-1] == "run":
                        del code[-1]
                        pointer = 0
                        pagot = int(input("Run how many lines? "))
                        shell()
                        while pointer < pagot:
                            pointer += 1
                            for i in code:
                                gawk = i.split()
                                del gawk[0]
                                gawk = " ".join(gawk)
                                if eval(i.split()[0]) == pointer:
                                    try:
                                        system(gawk)
                                    except Exception as e:
                                        if e != None:
                                            print(e)
                    elif code[-1] == "listcode":
                        del code[-1]
                        for i in code:
                            print(i)
                    elif code[-1] == "save":
                        del code[-1]
                        print(code)
                    elif code[-1] == "load":
                        del code[-1]
                        code = eval(input("Save code >>> "))
                    elif code[-1] == "new":
                        del code[-1]
                        code = []
                    else:
                        try:
                            run(code[-1].split(" "))
                        except Exception:
                            try:
                                system(code[-1])
                            except Exception as e:
                                if e != None:
                                    print(e)
                        del code[-1]
    elif x == 2:
        print("1 to execute normally")
        print("2 to execute coolly")
        x = int(input("\n"))
        if x == 1:
            del x, code, pointer
            shell()
            while True:
                try:
                    system(input("$ "))
                except Exception as e:
                    if e != None:
                        print(e)
        elif x == 2:
            system("cmd")
    elif x == 3:
        del x, code, pointer
        f = open(input("File name: "), "r")
        system(f.read())
        f.close()
elif x == 3:
    print("1 to run enhanced version")
    print("2 to execute single-line commands")
    print("3 to execute from files")
    x = int(input("\n"))
    if x == 1:
        print("You can run enhanced Brainf**k programs, like running AppleSoft BASIC in Apple ][. ")
        print("Write normal syntax, but start with a number that's the line number of the code line. ")
        print(
            "For example, like \"10 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++.-------------------.--.++++++++++++++++++.-.---------------.-.--------------------------------------------------------------------.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.-.------------------------------------------------------------------------------.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.---.+++++.---------.---------------------------------------------------------------------.+++++++++++++++++.-.\".\nThere's also some extra functions. ")
        print(
            "\"listcode\" command lists the entire code, and \"run\" runs the code in the lines from smallest to biggest. ")
        input("You can have a save code for your code and load it with \"save\" and \"load\" keywords. ")
        print("Use \"new\" syntax to clean your code.")
        shell()
        del x
        while True:
            kur = []
            for i in code:
                kur.append(i)
            for i in range(len(kur)):
                tul = kur[i]
                pul = tul.split()
                kur[i] = int(pul[0])
            code.append(input("\n> "))
            pul = code[-1].split()
            if pul[0].isnumeric():
                try:
                    del pul
                except NameError:
                    print("", end="")
                try:
                    del tul
                except NameError:
                    print("", end="")
                print("", end="")
            else:
                try:
                    del pul
                except NameError:
                    print("", end="")
                try:
                    del tul
                except NameError:
                    print("", end="")
                if code[-1] == "run":
                    del code[-1]
                    pointer = 0
                    pagot = int(input("Run how many lines? "))
                    shell()
                    while pointer < pagot:
                        pointer += 1
                        for i in code:
                            gawk = i.split()
                            del gawk[0]
                            gawk = " ".join(gawk)
                            if eval(i.split()[0]) == pointer:
                                bf(gawk, input("Input data >>> "))
                elif code[-1] == "listcode":
                    del code[-1]
                    for i in code:
                        print(i)
                elif code[-1] == "save":
                    del code[-1]
                    print(code)
                elif code[-1] == "load":
                    del code[-1]
                    code = eval(input("Save code >>> "))
                elif code[-1] == "new":
                    del code[-1]
                    code = []
                else:
                    bf(code[-1], input("Input data >>> "))
                    del code[-1]
    elif x == 2:
        del x, code, pointer
        shell()
        while True:
            bf(input(">>> "), input("input data: "))
    elif x == 3:
        del x, code, pointer
        f = open(input("File name of code: "), "r")
        g = open(input("File name of input data: "), "r")
        bf(f.read(), g.read())
        f.close()
        g.close()
elif x == 4:
    del x, code, pointer
    print("First, enter the compiling language as a Python list.")
    print("E.g. write \"[\"perl\", \"-e\"]\" to run Perl code. ")
    print("BASH -> \"bash\"")
    print("ZSH -> \"zsh\"")
    print("Fish -> \"fish\"")
    print("PowerShell -> \"pwsh\", or \"powershell\"")
    print("Batch -> \"cmd\" ")
    print("Swift -> \"swift\" ")
    print("Python -> \"python\", \"python3\"")
    print("Ruby -> \"ruby\"")
    print("Perl -> \"perl\"")
    print("PHP -> \"php\"")
    print("Lua -> \"lua\"")
    print("Node.js (JavaScript) -> \"node\" ")
    print("Java -> \"java\", \"javac\"")
    print("Kotlin -> \"kotlin\", \"kotlinc\"")
    print("Scala -> \"scala\" ")
    print("C# (C++++) -> \"dotnet run\", \"mono\"")
    print("F# (F++++) -> \"dotnet fsi\" ")
    print("Assembly (NASM) -> \"nasm\"")
    print("COBOL -> \"cobc -x\"")
    print("R -> \"Rscript\" ")
    print("Lisp (Common Lisp) -> \"sbcl\", \"clisp\"")
    print("Scheme -> \"racket\"")
    print("Prolog -> \"swipl\" ")
    print("PostgreSQL -> \"psql\"")
    print("MySQL -> \"mysql\"")
    input("SQLite -> \"sqlite3\" ")
    print(
        "Write the langs' list between \"quotation marks\", and all between [square braces] separated by, commas (like Python lists). ")
    print("E.g. write \"[\"perl\", \"-e\"]\" to make program write inline Perl -e code. ")
    print("Use \"[\"perl\", \"-c\"]\" this \"-c\" syntax to make the program run a code instead of a file. ")
    print("Then, give the file name to run, e.g. \"[\"python\", \"-c\", \"print('hello')\"]\"")
    input("So, basically text you need to enter to the \"subprocess.run()\" command. ")
    x = input("Get more information about subprocess.run() command? (y/n) ")
    if "y" in x.lower():
        help("subprocess.run")
    del x
    run(eval(input("Enter code: ")))
elif x == 5:
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
elif x == 6:
    print("1 to open Brainf**k")
    print("2 to open HQ9+")
    print("3 to open AlphaLang")
    print("4 to open PowerShell")
    print("5 to open WMI information shell")
    print("6 to open DeadFish")
    x = int(input("\n"))
    if x == 1:
        print("Brainf**k Syntax for this IDE:")
        print("""
+ Increment the value of the current cell
- Decrement the value of the current cell
> Move pointer to the right
< Move pointer to the left
. Print the Unicode character of the current cell
, Take user input (store in the current cell)
[ Jump past matching } if the current cell is 0
] Jump back to matching { if the current cell is not 0
; Print the raw value of the current cell (instead of Unicode)
# Set the current cell to zero
@ Duplicate the value of the current cell to the next cell
& Swap the current cell with the previous cell
% Multiply the current cell by 2
$ Divide the current cell by 2 (integer division)
^ Move the pointer to the first nonzero cell
~ Move the pointer to the last nonzero cell
( Push the current cell’s value onto a stack
) Pop the last value from the stack into the current cell
""")
        while True:
            x = input("code >>>     ")
            y = input("input data > ")
            bf(x, y)
    elif x == 2:
        print("HQ9+ Syntax for this IDE:")
        print(r"""
C Copies input to output.
H Prints "Hello, world!"
I Interprets input as program source.
Q Prints the program source code.
R Encrypts input with ROT-13.
S Sorts input lines randomly given from 1 to 10.
9 Prints the lyrics to "99 Bottles of Beer on the Wall."
+ Increments the accumulator.
- Decrements the accumulator.
* Doubles the accumulator.
/ Divides the accumulator by 3.
% Modulos the accumulator by n%2.
x Redefines the accumulator to its square.
X Redefines the accumulator to its cube.
& The / operation but int instead of float
A Print the accumulator
F Prints FizzBuzz up to 100.
- Dereferences a null pointer if preceded by an F.
$ Push the accumulator to the stack
# Pop a value from the stack and print it
^ Pop a value from the stack and print its ASCII value
= Print new line (\n in C++)
/ Get input from user and turn accumulator to it
P Get input from user and push string to stack
> Pop a value from the stack execute it in Python
< Pop a value from the stack evaluate it in Python
½ Pop a value from the stack and execute it in Batch
\ Get input from user and turn accumulator to its Unicode value
0 Turns accumulator to binary
2 Prints 2 and 3 timetable
G LGBTQ+ approved HQ9+ H
: Push accumulator's Unicode value to stack
; Append accumulator's Unicode value to stack's top value
""")
        """
        @ Repeat code after this 2 times.
        € Repeat code after this 3 times.
        é Repeat code after this infinitely.
        """
        while True:
            x = input(">>> ")
            hq(x)
    elif x == 3:
        print("AlphaLang Syntax:")
        print("""
AlphaLang is an esolang where every word is a syntax.
AlphaLang syntax is separated by spaces, and turns letters to integers.
E.g. syntax "abc" is "123" if translated to their numbers in alphabet.
1+2+3=6 so "abc" = 6 in AlphaLang. Each word corresponds to a function.
It's found according to their AlphaLang integer. Its memory system is a 1D grid.
It also has a pointer.
1 - 10	 Move the pointer to the right
11 - 20	 Move the pointer to the left
21 - 30	 Increment the memory cell at the pointer
31 - 40	 Decrement the memory cell at the pointer
41 - 50	 Output the Unicode value of the cell at the pointer
51 - 60  Output the value of the cell at the pointer
61 - 70	 Input a character and store it in the cell at the pointer
71 - 80  Input a number and store it in the cell at the pointer
81 - 90	 Jump past the matching 91-100 if the cell at the pointer is 0
91 - 100 Jump back to the matching 81-90 if the cell at the pointer isn't 0
""")
        dict = {chr(i + 96): i for i in range(1, 27)}
        while True:
            x = input(">>> ")
            list = x.split(" ")
            l = []
            for i in list:
                j = 0
                for k in range(len(i)):
                    try:
                        j += dict[i[k].lower()]
                    except KeyError:
                        pass
                l.append(j)
            memory = [0] * 256
            pointer = 0
            code = 0
            while code < len(l):
                i = l[code]
                if 1 <= i <= 10:
                    pointer = min(pointer + 1, 255)
                elif 11 <= i <= 20:
                    pointer = max(pointer - 1, 0)
                elif 21 <= i <= 30:
                    memory[pointer] += 1
                elif 31 <= i <= 40:
                    memory[pointer] -= 1
                elif 41 <= i <= 50:
                    print(chr(memory[pointer]), end="")
                elif 51 <= i <= 60:
                    print(memory[pointer])
                elif 61 <= i <= 70:
                    try:
                        memory[pointer] = ord(input()[0])
                    except Exception as e:
                        pass
                elif 71 <= i <= 80:
                    try:
                        memory[pointer] = int(input())
                    except Exception as e:
                        pass
                elif 81 <= i <= 90:
                    if memory[pointer] == 0:
                        open_loops = 1
                        while open_loops > 0:
                            code += 1
                            if code >= len(l):
                                break
                            if 81 <= l[code] <= 90:
                                open_loops += 1
                            elif 91 <= l[code] <= 100:
                                open_loops -= 1
                elif 91 <= i <= 100:
                    if memory[pointer] != 0:
                        close_loops = 1
                        while close_loops > 0:
                            code -= 1
                            if code < 0:
                                break
                            if 91 <= l[code] <= 100:
                                close_loops += 1
                            elif 81 <= l[code] <= 90:
                                close_loops -= 1
                code += 1
    elif x == 4:
        print("""
TOPIC
    Windows PowerShell Help System

SHORT DESCRIPTION
    Displays help about Windows PowerShell cmdlets and concepts.

LONG DESCRIPTION
    Windows PowerShell Help describes Windows PowerShell cmdlets,
    functions, scripts, and modules, and explains concepts, including
    the elements of the Windows PowerShell language.

    Windows PowerShell does not include help files, but you can read the
    help topics online, or use the Update-Help cmdlet to download help files
    to your computer and then use the Get-Help cmdlet to display the help
    topics at the command line.

    You can also use the Update-Help cmdlet to download updated help files
    as they are released so that your local help content is never obsolete.

    Without help files, Get-Help displays auto-generated help for cmdlets,
    functions, and scripts.


  ONLINE HELP
    You can find help for Windows PowerShell online in the TechNet Library
    beginning at http://go.microsoft.com/fwlink/?LinkID=108518.

    To open online help for any cmdlet or function, type:

        Get-Help <cmdlet-name> -Online

  UPDATE-HELP
    To download and install help files on your computer:

       1. Start Windows PowerShell with the "Run as administrator" option.
       2. Type:

          Update-Help

    After the help files are installed, you can use the Get-Help cmdlet to
    display the help topics. You can also use the Update-Help cmdlet to
    download updated help files so that your local help files are always
    up-to-date.

    For more information about the Update-Help cmdlet, type:

       Get-Help Update-Help -Online

    or go to: http://go.microsoft.com/fwlink/?LinkID=210614


  GET-HELP
    The Get-Help cmdlet displays help at the command line from content in
    help files on your computer. Without help files, Get-Help displays basic
    help about cmdlets and functions. You can also use Get-Help to display
    online help for cmdlets and functions.

    To get help for a cmdlet, type:

        Get-Help <cmdlet-name>

    To get online help, type:

        Get-Help <cmdlet-name> -Online

    The titles of conceptual topics begin with "About_".
    To get help for a concept or language element, type:

        Get-Help About_<topic-name>

    To search for a word or phrase in all help files, type:

        Get-Help <search-term>

    For more information about the Get-Help cmdlet, type:

        Get-Help Get-Help -Online

    or go to: http://go.microsoft.com/fwlink/?LinkID=113316


  EXAMPLES:
      Save-Help              : Download help files from the Internet and saves
                               them on a file share.
      Update-Help            : Downloads and installs help files from the
                               Internet or a file share.
      Get-Help Get-Process   : Displays help about the Get-Process cmdlet.
      Get-Help Get-Process -Online
                             : Opens online help for the Get-Process cmdlet.
      Help Get-Process       : Displays help about Get-Process one page at a time.
      Get-Process -?         : Displays help about the Get-Process cmdlet.
      Get-Help About_Modules : Displays help about Windows PowerShell modules.
      Get-Help remoting      : Searches the help topics for the word "remoting."

  SEE ALSO:
      about_Updatable_Help
      Get-Help
      Save-Help
      Update-Help
For more information on a specific command, type HELP command-name
ASSOC          Displays or modifies file extension associations.
ATTRIB         Displays or changes file attributes.
BREAK          Sets or clears extended CTRL+C checking.
BCDEDIT        Sets properties in boot database to control boot loading.
CACLS          Displays or modifies access control lists (ACLs) of files.
CALL           Calls one batch program from another.
CD             Displays the name of or changes the current directory.
CHCP           Displays or sets the active code page number.
CHDIR          Displays the name of or changes the current directory.
CHKDSK         Checks a disk and displays a status report.
CHKNTFS        Displays or modifies the checking of disk at boot time.
CLS            Clears the screen.
CMD            Starts a new instance of the Windows command interpreter.
COLOR          Sets the default console foreground and background colors.
COMP           Compares the contents of two files or sets of files.
COMPACT        Displays or alters the compression of files on NTFS partitions.
CONVERT        Converts FAT volumes to NTFS.  You cannot convert the
               current drive.
COPY           Copies one or more files to another location.
DATE           Displays or sets the date.
DEL            Deletes one or more files.
DIR            Displays a list of files and subdirectories in a directory.
DISKPART       Displays or configures Disk Partition properties.
DOSKEY         Edits command lines, recalls Windows commands, and 
               creates macros.
DRIVERQUERY    Displays current device driver status and properties.
ECHO           Displays messages, or turns command echoing on or off.
ENDLOCAL       Ends localization of environment changes in a batch file.
ERASE          Deletes one or more files.
EXIT           Quits the CMD.EXE program (command interpreter).
FC             Compares two files or sets of files, and displays the 
               differences between them.
FIND           Searches for a text string in a file or files.
FINDSTR        Searches for strings in files.
FOR            Runs a specified command for each file in a set of files.
FORMAT         Formats a disk for use with Windows.
FSUTIL         Displays or configures the file system properties.
FTYPE          Displays or modifies file types used in file extension 
               associations.
GOTO           Directs the Windows command interpreter to a labeled line in 
               a batch program.
GPRESULT       Displays Group Policy information for machine or user.
HELP           Provides Help information for Windows commands.
ICACLS         Display, modify, backup, or restore ACLs for files and 
               directories.
IF             Performs conditional processing in batch programs.
LABEL          Creates, changes, or deletes the volume label of a disk.
MD             Creates a directory.
MKDIR          Creates a directory.
MKLINK         Creates Symbolic Links and Hard Links
MODE           Configures a system device.
MORE           Displays output one screen at a time.
MOVE           Moves one or more files from one directory to another 
               directory.
OPENFILES      Displays files opened by remote users for a file share.
PATH           Displays or sets a search path for executable files.
PAUSE          Suspends processing of a batch file and displays a message.
POPD           Restores the previous value of the current directory saved by 
               PUSHD.
PRINT          Prints a text file.
PROMPT         Changes the Windows command prompt.
PUSHD          Saves the current directory then changes it.
RD             Removes a directory.
RECOVER        Recovers readable information from a bad or defective disk.
REM            Records comments (remarks) in batch files or CONFIG.SYS.
REN            Renames a file or files.
RENAME         Renames a file or files.
REPLACE        Replaces files.
RMDIR          Removes a directory.
ROBOCOPY       Advanced utility to copy files and directory trees
SET            Displays, sets, or removes Windows environment variables.
SETLOCAL       Begins localization of environment changes in a batch file.
SC             Displays or configures services (background processes).
SCHTASKS       Schedules commands and programs to run on a computer.
SHIFT          Shifts the position of replaceable parameters in batch files.
SHUTDOWN       Allows proper local or remote shutdown of machine.
SORT           Sorts input.
START          Starts a separate window to run a specified program or command.
SUBST          Associates a path with a drive letter.
SYSTEMINFO     Displays machine specific properties and configuration.
TASKLIST       Displays all currently running tasks including services.
TASKKILL       Kill or stop a running process or application.
TIME           Displays or sets the system time.
TITLE          Sets the window title for a CMD.EXE session.
TREE           Graphically displays the directory structure of a drive or 
               path.
TYPE           Displays the contents of a text file.
VER            Displays the Windows version.
VERIFY         Tells Windows whether to verify that your files are written
               correctly to a disk.
VOL            Displays a disk volume label and serial number.
XCOPY          Copies files and directory trees.
WMIC           Displays WMI information inside interactive command shell.

For more information on tools see the command-line reference in the online help.
""")
        system("cmd")
    elif x == 5:
        print("""
[global switches] <command>

The following global switches are available:
/NAMESPACE           Path for the namespace the alias operate against.
/ROLE                Path for the role containing the alias definitions.
/NODE                Servers the alias will operate against.
/IMPLEVEL            Client impersonation level.
/AUTHLEVEL           Client authentication level.
/LOCALE              Language id the client should use.
/PRIVILEGES          Enable or disable all privileges.
/TRACE               Outputs debugging information to stderr.
/RECORD              Logs all input commands and output.
/INTERACTIVE         Sets or resets the interactive mode.
/FAILFAST            Sets or resets the FailFast mode.
/USER                User to be used during the session.
/PASSWORD            Password to be used for session login.
/OUTPUT              Specifies the mode for output redirection.
/APPEND              Specifies the mode for output redirection.
/AGGREGATE           Sets or resets aggregate mode.
/AUTHORITY           Specifies the <authority type> for the connection.
/?[:<BRIEF|FULL>]    Usage information.

For more information on a specific global switch, type: switch-name /?


The following alias/es are available in the current role:
ALIAS                    - Access to the aliases available on the local system
BASEBOARD                - Base board (also known as a motherboard or system board) management.
BIOS                     - Basic input/output services (BIOS) management.
BOOTCONFIG               - Boot configuration management.
CDROM                    - CD-ROM management.
COMPUTERSYSTEM           - Computer system management.
CPU                      - CPU management.
CSPRODUCT                - Computer system product information from SMBIOS. 
DATAFILE                 - DataFile Management.  
DCOMAPP                  - DCOM Application management.
DESKTOP                  - User's Desktop management.
DESKTOPMONITOR           - Desktop Monitor management.
DEVICEMEMORYADDRESS      - Device memory addresses management.
DISKDRIVE                - Physical disk drive management. 
DISKQUOTA                - Disk space usage for NTFS volumes.
DMACHANNEL               - Direct memory access (DMA) channel management.
ENVIRONMENT              - System environment settings management.
FSDIR                    - Filesystem directory entry management. 
GROUP                    - Group account management. 
IDECONTROLLER            - IDE Controller management.  
IRQ                      - Interrupt request line (IRQ) management. 
JOB                      - Provides  access to the jobs scheduled using the schedule service. 
LOADORDER                - Management of system services that define execution dependencies. 
LOGICALDISK              - Local storage device management.
LOGON                    - LOGON Sessions.  
MEMCACHE                 - Cache memory management.
MEMORYCHIP               - Memory chip information.
MEMPHYSICAL              - Computer system's physical memory management. 
NETCLIENT                - Network Client management.
NETLOGIN                 - Network login information (of a particular user) management. 
NETPROTOCOL              - Protocols (and their network characteristics) management.
NETUSE                   - Active network connection management.
NIC                      - Network Interface Controller (NIC) management.
NICCONFIG                - Network adapter management. 
NTDOMAIN                 - NT Domain management.  
NTEVENT                  - Entries in the NT Event Log.  
NTEVENTLOG               - NT eventlog file management. 
ONBOARDDEVICE            - Management of common adapter devices built into the motherboard (system board).
OS                       - Installed Operating System/s management. 
PAGEFILE                 - Virtual memory file swapping management. 
PAGEFILESET              - Page file settings management. 
PARTITION                - Management of partitioned areas of a physical disk.
PORT                     - I/O port management.
PORTCONNECTOR            - Physical connection ports management.
PRINTER                  - Printer device management. 
PRINTERCONFIG            - Printer device configuration management.  
PRINTJOB                 - Print job management. 
PROCESS                  - Process management. 
PRODUCT                  - Installation package task management. 
QFE                      - Quick Fix Engineering.  
QUOTASETTING             - Setting information for disk quotas on a volume. 
RDACCOUNT                - Remote Desktop connection permission management.
RDNIC                    - Remote Desktop connection management on a specific network adapter.
RDPERMISSIONS            - Permissions to a specific Remote Desktop connection.
RDTOGGLE                 - Turning Remote Desktop listener on or off remotely.
RECOVEROS                - Information that will be gathered from memory when the operating system fails. 
REGISTRY                 - Computer system registry management.
SCSICONTROLLER           - SCSI Controller management.  
SERVER                   - Server information management. 
SERVICE                  - Service application management. 
SHADOWCOPY               - Shadow copy management.
SHADOWSTORAGE            - Shadow copy storage area management.
SHARE                    - Shared resource management. 
SOFTWAREELEMENT          - Management of the  elements of a software product installed on a system.
SOFTWAREFEATURE          - Management of software product subsets of SoftwareElement. 
SOUNDDEV                 - Sound Device management.
STARTUP                  - Management of commands that run automatically when users log onto the computer system.
SYSACCOUNT               - System account management.  
SYSDRIVER                - Management of the system driver for a base service.
SYSTEMENCLOSURE          - Physical system enclosure management.
SYSTEMSLOT               - Management of physical connection points including ports,  slots and peripherals, and proprietary connections points.
TAPEDRIVE                - Tape drive management.  
TEMPERATURE              - Data management of a temperature sensor (electronic thermometer).
TIMEZONE                 - Time zone data management. 
UPS                      - Uninterruptible power supply (UPS) management. 
USERACCOUNT              - User account management.
VOLTAGE                  - Voltage sensor (electronic voltmeter) data management.
VOLUME                   - Local storage volume management.
VOLUMEQUOTASETTING       - Associates the disk quota setting with a specific disk volume. 
VOLUMEUSERQUOTA          - Per user storage volume quota management.
WMISET                   - WMI service operational parameters management. 

For more information on a specific alias, type: alias /?

CLASS     - Escapes to full WMI schema.
PATH      - Escapes to full WMI object paths.
CONTEXT   - Displays the state of all the global switches.
QUIT/EXIT - Exits the program.

For more information on CLASS/PATH/CONTEXT, type: (CLASS | PATH | CONTEXT) /?
""")
        system("wmic")
    elif x == 6:
        print("DeadFish Syntax for this IDE:")
        print("""
i Increment the accumulator by 1
d Decrement the accumulator by 1
s Multiply the accumulator by itself
o Display the accumulator as integer
ö Display the accumulator as integer without newline
h Halt
x Return to FOS main menu
I Begin statement def
D Set accumulator to 0
S End statement def
O Display accumulator as Unicode character
Ö Display accumulator as Unicode character without newline
H Define statement name
? Print statement name
! Print statement function
Statement definitions:
    I Hv ii S vvv o h

    Here, a statement's defined with I.
    Its name is selected "v" using the H operator.
    Its role is "ii", meaning it increments the accumulator by 2.
    Its definition is finished with S.
    It's used 3 times as "vvv".
    So when printed with o, it'll output "6" (3*2).
    Then, program's halted with "h".
WARNING: Statements can't be nested in this IDE.
""")
        while True:
            code = input(">>> ")
            if df(code) == 1:
                print("Exit code: 1\nProgram was manually halted by user.")
            else:
                print("Exit code: 0\nProgram compiled successfully.")
"""
language list:
english
sanskrit
basque
tagalog
classical nahuatl
georgian
kwakiutl
volapuk
latin
"""
