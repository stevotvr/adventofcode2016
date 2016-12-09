x = y = direction = 0
moves = open('input.txt', 'r').readline().strip().split(', ')
visited = set((0, 0))

for move in moves:
    if move[0] == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    elif move[0] == 'R':
        if direction == 3:
            direction = 0
        else:
            direction += 1

    dist = int(''.join(move[1:]))
    for _ in range(dist):
        if direction == 0:
            y -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1

        if (x, y) in visited:
            print(abs(x) + abs(y))
            input()
            exit()
        else:
            visited.add((x, y))
