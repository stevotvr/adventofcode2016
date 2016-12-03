valid = 0
values = []

for line in open('input.txt', 'r'):
	values = values + [int(x.strip()) for x in line.split()]

i = 0
while i < len(values) - 6:
	sides = [values[i], values[i + 3], values[i + 6]]
	sides.sort()
	i = i + 7 if (i + 1) % 3 == 0 else i + 1
	if sides[0] + sides[1] > sides[2]:
		valid = valid + 1

print(valid)
input()
