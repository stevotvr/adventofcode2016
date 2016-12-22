import re

class Node:
    def __init__(self, x, y, size, used):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = size - used

nodes = []
empty = None
for line in open('input.txt', 'r'):
    m = re.search(r'node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T', line)
    if m == None:
        continue
    node = Node(*map(int, m.group(1, 2, 3, 4)))
    if node.x == len(nodes):
        nodes.append([])
    nodes[node.x].append(node)
    if node.used == 0:
        empty = (node.x, node.y)

moves = 0
x, y = empty
while y > 0:
    if nodes[x][y - 1].used <= nodes[x][y].size:
        moves += 1
        y -= 1
    else:
        for i in range(1, max(x, len(nodes) - x)):
            if x + i < len(nodes) and nodes[x + i][y - 1].used <= nodes[x][y].size:
                moves += 2 + i * 2
                y -= 2
                break
            if x - i > 0 and nodes[x - i][y - 1].used <= nodes[x][y].size:
                moves += 2 + i * 2
                y -= 2
                break

moves += len(nodes) - 1 - x
moves += 5 * (len(nodes) - 2)

print(moves)
input()
