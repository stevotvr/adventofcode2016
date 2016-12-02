keys = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
x = y = 1
numbers = []

for line in open('input.txt', 'r'):
	for c in line:
		if c == 'U':
			y = max(0, y - 1)
		elif c == 'D':
			y = min(2, y + 1)
		elif c == 'L':
			x = max(0, x - 1)
		elif c == 'R':
			x = min(2, x + 1)
	numbers.append(str(keys[y][x]))

print(''.join(numbers))
input()
