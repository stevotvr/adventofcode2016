addr = 0
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

instructions = [line.split() for line in open('input.txt', 'r')]

while addr < len(instructions):
    line = instructions[addr]
    if line[0] == 'cpy':
        registers[line[2]] = int(line[1]) if line[1].isnumeric() else registers[line[1]]
        addr += 1
    elif line[0] == 'inc':
        registers[line[1]] += 1
        addr += 1
    elif line[0] == 'dec':
        registers[line[1]] -= 1
        addr += 1
    elif line[0] == 'jnz':
        if line[1] != '0' and (line[1].isnumeric() or registers[line[1]] != 0):
            addr += int(line[2])
        else:
            addr += 1

print(registers['a'])
input()
