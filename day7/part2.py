count = 0

for line in open('input.txt', 'r'):
    inBraces = False
    abas = []
    hypernet = []
    for i in range(len(line.strip()) - 2):
        if line[i] == '[':
            inBraces = True
            continue
        if line[i] == ']':
            inBraces = False
            continue

        if inBraces:
            hypernet.append(line[i])
        elif line[i] == line[i + 2] and line[i] != line[i + 1]:
            abas.append(line[i:i + 3])

    hypernet = ''.join(hypernet)
    for aba in abas:
        if aba[1] + aba[0] + aba[1] in hypernet:
            count = count + 1
            break

print(count)
input()
