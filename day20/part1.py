ranges = []
for line in open('input.txt', 'r'):
    ranges.append(tuple(map(int, line.split('-'))))
ranges.sort()

lowest = 0
for l, r in ranges:
    if l <= lowest <= r:
        lowest = r + 1

print(lowest)
input()
