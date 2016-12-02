keys = [
[' ', ' ', '1', ' ', ' '],
[' ', '2', '3', '4', ' '],
['5', '6', '7', '8', '9'],
[' ', 'A', 'B', 'C', ' '],
[' ', ' ', 'D', ' ', ' ']
]
x = testX = 0
y = testY = 2
numbers = []

for line in open('input.txt', 'r'):
	for c in line:
		testX = x
		testY = y
		if c == 'U':
			testY = max(0, y - 1)
		elif c == 'D':
			testY = min(4, y + 1)
		elif c == 'L':
			testX = max(0, x - 1)
		elif c == 'R':
			testX = min(4, x + 1)

		if keys[testY][testX] != ' ':
			x = testX
			y = testY

	numbers.append(keys[y][x])

print(''.join(numbers))
input()
