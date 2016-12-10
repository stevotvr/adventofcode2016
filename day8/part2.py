import os
import time

os.system('cls')

rows = 6
cols = 50

grid = []
for _ in range(rows):
    grid.append([False] * cols)

for line in open('input.txt', 'r'):
    if line.startswith('rect'):
        (a, b) = line[4:].strip().split('x')
        for i in range(int(b)):
            for j in range(int(a)):
                grid[i][j] = True
    elif line.startswith('rotate row'):
        (a, b) = line[13:].strip().split(' by ')
        rowCopy = [False] * cols
        for i in range(cols):
            rowCopy[(i + int(b)) % cols] = grid[int(a)][i]
        grid[int(a)] = rowCopy
    elif line.startswith('rotate column'):
        (a, b) = line[16:].strip().split(' by ')
        colCopy = [False] * rows
        for i in range(rows):
            colCopy[(i + int(b)) % rows] = grid[i][int(a)]
        for i in range(rows):
            grid[i][int(a)] = colCopy[i]
    print('\033[1;1H' + '\n'.join([''.join(['█' if cell else '░' for cell in row]) for row in grid]))
    time.sleep(0.05)

print('Done!')
input()
