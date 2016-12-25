addr = 0
registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}

instructions = [line.split() for line in open('input.txt', 'r')]
toggleMap = {'inc': 'dec', 'dec': 'inc', 'tgl': 'inc', 'cpy': 'jnz', 'jnz': 'cpy'}

def cpy(x, y):
    if y not in registers:
        return
    registers[y] = registers[x] if x in registers else int(x)

def inc(x):
    registers[x] += 1

def dec(x):
    registers[x] -= 1

def jnz(x, y):
    global addr
    if x != '0' and (x not in registers or registers[x] != 0):
        addr += registers[y] if y in registers else int(y)
    else:
        addr += 1 

def tgl(x):
    global addr
    target = addr + (registers[x] if x in registers else int(x))
    if 0 <= target < len(instructions):
        instructions[target][0] = toggleMap[instructions[target][0]]

while addr < len(instructions):
    line = instructions[addr]
    if line[0] == 'cpy':
        cpy(line[1], line[2])
        addr += 1
    elif line[0] == 'inc':
        inc(line[1])
        addr += 1
    elif line[0] == 'dec':
        dec(line[1])
        addr += 1
    elif line[0] == 'jnz':
        jnz(line[1], line[2])
    elif line[0] == 'tgl':
        tgl(line[1])
        addr += 1

print(registers['a'])
input()
