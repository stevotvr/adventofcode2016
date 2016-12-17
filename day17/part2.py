from hashlib import md5

inp = 'yjjvjgan'
openChars = 'bcdef'

def getValidDirections(x, y, path):
    m = md5()
    m.update(bytes(inp + ''.join(path), 'utf-8'))
    hash = m.hexdigest()
    dirs = []
    if y > 0 and hash[0] in openChars:
        dirs.append((x, y - 1, path + tuple('U')))
    if y < 3 and hash[1] in openChars:
        dirs.append((x, y + 1, path + tuple('D')))
    if x > 0 and hash[2] in openChars:
        dirs.append((x - 1, y, path + tuple('L')))
    if x < 3 and hash[3] in openChars:
        dirs.append((x + 1, y, path + tuple('R')))
    return dirs

visited = set()
stack = [(0, 0, ())]
valid = set()
while stack:
    state = stack.pop()
    if state[0] == state[1] == 3:
        valid.add(''.join(state[2]))
        continue
    visited.add(state)
    for dir in getValidDirections(*state):
        if dir not in visited:
            stack.append(dir)

print(max([len(x) for x in valid]))
input()
