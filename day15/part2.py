import re

discs = []
for line in open('input.txt', 'r'):
    m = re.search(r'Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)', line)
    discs.append((int(m.group(1)), int(m.group(2))))
discs.append((11, 0))

time = 0
while True:
    positions = [(discs[i][1] + time + i + 1) % discs[i][0] for i in range(len(discs))]
    if max(positions) == 0:
        break
    time += max([discs[i][0] - positions[i] for i in range(len(discs))])

print(time)
input()
