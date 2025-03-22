# head (module importing that is necessary to define functions for module)

from time import sleep
from random import randint, shuffle
from sys import platform
xoxguide = {"A" : "⬜", "X" : "❌", "O" : "⭕"}

# body (function defining for module)

def operation(string):
    x = float(input("Number 1: "))
    y = float(input("Number 2: "))
    z = eval(f"x {string} y")
    if int(z) == z:
        z = int(z)
    print(f"Operation Result:\n{z}")
def sqrt():
    x = float(input("Number 1: "))
    y = float(input("Number 2: "))
    z = eval(f"x ** (1 / y)")
    if int(z) == z:
        z = int(z)
    print(f"Operation Result:\n{z}")
def edit(str, edit):
    txt = str
    return eval(f"{txt}.{edit}()")
def get(xox):
    print(xox[0], xox[1], xox[2], "   ", xoxguide[xox[0]], xoxguide[xox[1]], xoxguide[xox[2]])
    print(xox[3], xox[4], xox[5], "   ", xoxguide[xox[3]], xoxguide[xox[4]], xoxguide[xox[5]])
    print(xox[6], xox[7], xox[8], "   ", xoxguide[xox[6]], xoxguide[xox[7]], xoxguide[xox[8]])
def o(xox):
    print("O to move")
    x = int(input("Where to place o? (1/9) "))
    if xox[x - 1] != "A":
        print("Invalid position")
        o(xox)
    else:
        xox[x - 1] = "O"
def xx(xox):
    print("X to move")
    x = int(input("Where to place x? (1/9) "))
    if xox[x - 1] != "A":
        print("Invalid position")
        xx(xox)
    else:
        xox[x - 1] = "X"
def ai(xox):
    print("O (computer) to move")
    x = randint(1, 9)
    if xox[x - 1] != "A":
        aipatch(xox)
    else:
        xox[x - 1] = "O"
def aipatch(xox):
    x = randint(1, 9)
    if xox[x - 1] != "A":
        aipatch(xox)
    else:
        xox[x - 1] = "O"
def scramble(x):
    list = []
    for i in range(len(x)):
        list.append(x[i])
    shuffle(list)
    y = ""
    for i in list:
        y = f"{y}{i}"
    return y
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
xyz = ["+", "-", "*", "/", "%", "**", "//"]
class Life:
    def __init__(self, g1, g2):
        self.tf = {False : 0, True : 1}
        self.dict = {0: g1, 1: g2}
        self.grid = []
        for i in range(10 * 10):
            if (i + 1) % 10 == 0 or (i + 1) % 10 == 1 or i < 11 or i > 89:
                self.grid.append(0)
            else:
                self.grid.append(randint(0, 1))
    def dead(self, grid, int):
        return grid[int] == 0
    def alive(self, grid, int):
        return grid[int] == 1
    def print(self):
        for i in range(len(self.grid)):
            if (i + 1) % 10 == 0:
                print(self.dict[self.grid[i]])
            else:
                print(self.dict[self.grid[i]], end = "")
        print()
    def nb(self, grid, int):
        nb = 0
        self.tf = {False : 0, True : 1}
        if (int + 1) % 10 == 1:
            x = int - 10
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int - 9
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int + 1
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int + 10
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int + 11
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
        elif (int + 1) % 10 == 0:
            x = int - 11
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int - 10
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int - 1
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int + 9
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
            x = int + 10
            try:
                if not ("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError:
                pass
        else:
            x = int - 11
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int - 10
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int - 9
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int - 1
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int + 1
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int + 9
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int + 10
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
            x = int + 11
            try:
                if not("-" in str(x)): nb += self.tf[grid[x] == 1]
            except IndexError: pass
        return nb
    def kill(self, grid, int):
        grid[int] = 0
    def live(self, grid, int):
        grid[int] = 1
    def ctrl(self, grid, int):
        if self.alive(grid, int):
            if self.nb(grid, int) < 2:
                self.kill(grid, int) # underpopulation
            elif self.nb(grid, int) > 3:
                self.kill(grid, int) # overpopulation
        elif self.dead(grid, int):
            if self.nb(grid, int) == 2 or self.nb(grid, int) == 3:
                self.live(grid, int) # reproduction
    def loop(self, grid, int):
        while True:
            self.old = grid.copy()
            for i in range(len(grid)):
                self.ctrl(grid, i)
            self.print()
            sleep(int)
            if self.old == self.grid:
                break
def shell():
    print(f'Python 3.8.5 (default, Jul 20 2020, 23:11:29) [GCC 9.3.0] on {platform}\nType "help", "copyright", "credits" or "license" for more information.')
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
def factor(x):
    factor = []
    for i in range(1, x + 1):
        if x % i == 0:
            factor.append(i)
    return factor
