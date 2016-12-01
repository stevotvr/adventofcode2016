x = y = direction = 0
moves = open('input.txt', 'r').readline().strip().split(', ')

for move in moves:
	if move[0] == 'L':
		if direction == 0:
			direction = 3
		else:
			direction -= 1
	elif move[0] == 'R':
		if direction == 3:
			direction = 0
		else:
			direction += 1

	dist = int(''.join(move[1:]))
	if direction == 0:
		y -= dist
	elif direction == 1:
		x += dist
	elif direction == 2:
		y += dist
	elif direction == 3:
		x -= dist

print(abs(x) + abs(y))
input()
