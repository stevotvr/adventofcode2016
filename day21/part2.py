import re

password = list('fbgdceah')

instructions = []
for line in open('input.txt', 'r'):
    instructions.append(line)
instructions.reverse()

rotMap = [7, 7, 2, 6, 1, 5, 0, 4]
for line in instructions:
    if line.startswith('swap position'):
        x, y = map(int, re.findall(r'\b\d+\b', line))
        password[x], password[y] = password[y], password[x]
    elif line.startswith('swap letter'):
        x, y = re.findall(r'\b\w\b', line)
        for i in range(len(password)):
            if password[i] == x:
                password[i] = y
            elif password[i] == y:
                password[i] = x
    elif line.startswith('rotate based'):
        x = line.strip()[-1]
        rot = rotMap[password.index(x)]
        password = password[-rot:] + password[0:-rot]
    elif line.startswith('rotate'):
        x = int(re.findall(r'\b\d+\b', line)[0])
        x %= len(password)
        if 'left' in line:
            password = password[-x:] + password[0:-x]
        else:
            password = password[x:] + password[0:x]
    elif line.startswith('reverse'):
        x, y = map(int, re.findall(r'\b\d+\b', line))
        password[x:y + 1] = reversed(password[x:y + 1])
    elif line.startswith('move'):
        x, y = map(int, re.findall(r'\b\d\b', line))
        password.insert(x, password.pop(y))

print(''.join(password))
input()
