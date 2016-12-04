total = 0

for line in open('input.txt', 'r'):
	valid = True
	line = line.strip().replace('[', '-')[0:-1]
	(name, sector, check) = line.rsplit('-', 2)
	name = name.replace('-', '')

	counts = dict()
	for c in name:
		counts[c] = counts.get(c, 0) + 1

	ranked = list(counts.items())
	ranked.sort(key=lambda t: t[0])
	ranked.sort(key=lambda t: t[1], reverse=True)
	for i in range(len(check)):
		if ranked[i][0] != check[i]:
			valid = False
			break

	if valid:
		total = total + int(sector)

print(total)
input()
