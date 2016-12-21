import re

password = list('abcdefgh')

for line in open('input.txt', 'r'):
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
        rot = 1 + password.index(x)
        if rot > 4:
            rot += 1
        rot %= len(password)
        password = password[-rot:] + password[0:-rot]
    elif line.startswith('rotate'):
        x = int(re.findall(r'\b\d+\b', line)[0])
        x %= len(password)
        if 'right' in line:
            password = password[-x:] + password[0:-x]
        else:
            password = password[x:] + password[0:x]
    elif line.startswith('reverse'):
        x, y = map(int, re.findall(r'\b\d+\b', line))
        password[x:y + 1] = reversed(password[x:y + 1])
    elif line.startswith('move'):
        x, y = map(int, re.findall(r'\b\d\b', line))
        password.insert(y, password.pop(x))

print(''.join(password))
input()
