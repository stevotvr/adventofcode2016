addr = 0
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

instructions = [line.split() for line in open('input.txt', 'r')]

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

def out(x):
    if x in registers:
        return registers[x]
    else:
        return int(x)

initA = 0
output = None
counter = 0
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
    elif line[0] == 'out':
        nextOut = out(line[1])
        if (output == None and nextOut not in (0, 1)) or (output == 0 and nextOut != 1) or (output == 1 and nextOut != 0):
            initA += 1
            output = None
            addr = counter = 0
            registers = {'a': initA, 'b': 0, 'c': 0, 'd': 0}
        else:
            counter += 1
            if counter > 200:
                break
            output = nextOut
            addr += 1

print(initA)
input()
