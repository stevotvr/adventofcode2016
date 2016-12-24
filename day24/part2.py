from itertools import permutations

maze = []
points = set()
start = None

for line in open('input.txt', 'r'):
    maze.append(list(line.strip()))
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j].isdigit():
            if maze[i][j] == '0':
                start = (i, j)
            else:
                points.add((i, j))
        maze[i][j] = maze[i][j] != '#'

def isWall(pos):
    if 0 < pos[0] < len(maze) - 1 and 0 < pos[1] < len(maze[pos[0]]) - 1:
        return not maze[pos[0]][pos[1]]
    return True

distances = dict()
def bfs(start, dest):
    if (start, dest) in distances:
        return distances[(start, dest)]
    stack = [(start, 0)]
    visited = set([start])
    while stack:
        position, dist = stack.pop(0)
        if position == dest:
            distances[(start, dest)] = dist
            distances[(dest, start)] = dist
            return dist
        x, y = position
        dist += 1
        for next in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if not isWall(next) and next not in visited:
                stack.append((next, dist))
                visited.add(next)

minimum = 2**64
for p in permutations(points):
    dist = bfs(start, p[0])
    for i in range(1, len(p)):
        dist += bfs(p[i - 1], p[i])
        if dist > minimum:
            dist = 0
            break
    if dist:
        minimum = min(minimum, dist + bfs(p[-1], start))

print(minimum)
input()
