valid = 0

for line in open('input.txt', 'r'):
	sides = [int(x.strip()) for x in line.split()]
	sides.sort()
	if sides[0] + sides[1] > sides[2]:
		valid = valid + 1

print(valid)
input()
