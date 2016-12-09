count = 0

for line in open('input.txt', 'r'):
    inBraces = False
    valid = False
    for i in range(len(line.strip()) - 3):
        if '[' in line[i:i + 3]:
            inBraces = True
            continue
        if ']' in line[i:i + 3]:
            inBraces = False
            continue
        if line[i] == line[i + 3] and line[i + 1] == line[i + 2] and line[i] != line[i + 1]:
            if inBraces:
                valid = False
                break
            else:
                valid = True
    if valid:
        count = count + 1

print(count)
input()
