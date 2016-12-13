inp = 1352

def isWall(pos):
    x, y = pos
    if x < 0 or y < 0:
        return True
    number = x * x + 3 * x + 2 * x * y + y + y * y
    number += inp
    return len([d for d in bin(number)[2:] if d == '1']) % 2 == 1

visited = set()
stack = [(0, (1, 1))]
while stack:
    d, p = stack.pop(0)
    if p == (31, 39):
        print(d)
        break
    visited.add(p)
    x, y = p
    for i in (-1, 1):
        np = (x + i, y)
        if np not in visited and not isWall(np):
            stack.append((d + 1, np))
        np = (x, y + i)
        if np not in visited and not isWall(np):
            stack.append((d + 1, np))

input()
