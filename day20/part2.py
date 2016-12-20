ranges = []
for line in open('input.txt', 'r'):
    ranges.append(list(map(int, line.split('-'))))
ranges.sort()

i = 0
while i < len(ranges) - 1:
    if ranges[i][1] >= ranges[i + 1][0] - 1:
        ranges[i][1] = max(ranges[i][1], ranges[i + 1][1])
        ranges.pop(i + 1)
    else:
        i += 1

allowed = 4294967296
for l, r in ranges:
    allowed -= r - l + 1

print(allowed)
input()
