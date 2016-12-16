inp = '11101000110010100'
output = list(inp)

while len(output) < 272:
    output += ['0'] + ['0' if x == '1' else '1' for x in reversed(output)]
output = output[0:272]

while len(output) % 2 == 0:
    output = ['1' if output[i] == output[i + 1] else '0' for i in range(0, len(output), 2)]

print(''.join(output))
input()
