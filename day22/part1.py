import re

class Node:
    def __init__(self, x, y, size, used):
        self.x = x
        self.y = y
        self.size = size
        self.used = used

nodes = []
for line in open('input.txt', 'r'):
    m = re.search(r'node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T', line)
    if m == None:
        continue
    nodes.append(Node(*map(int, m.group(1, 2, 3, 4))))

paired = set()
pairs = 0
for a in nodes:
    if not a.size or a in paired:
        continue
    for b in nodes:
        if a == b:
            continue
        if a.used <= b.size - b.used:
            paired.add(a)
            paired.add(b)
            pairs += 1

print(pairs)
input()
