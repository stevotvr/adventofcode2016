currentRow = [x == '^' for x in open('input.txt', 'r').readline()]
traps = ((True, True, False), (False, True, True), (True, False, False), (False, False, True))

safeTiles = currentRow.count(False)
for _ in range(39):
    nextRow = []
    for i in range(len(currentRow)):
        l, c, r = i > 0 and currentRow[i - 1], currentRow[i], i < len(currentRow) - 1 and currentRow[i + 1]
        nextRow.append((l, c, r) in traps)
    safeTiles += nextRow.count(False)
    currentRow = nextRow

print(safeTiles)
input()
