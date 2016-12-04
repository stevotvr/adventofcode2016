for line in open('input.txt', 'r'):
	valid = True
	line = line.strip().replace('[', '-')[0:-1]
	(name, sector, check) = line.rsplit('-', 2)

	counts = dict()
	for c in name:
		if c == '-':
			continue
		counts[c] = counts.get(c, 0) + 1

	ranked = list(counts.items())
	ranked.sort(key=lambda t: t[0])
	ranked.sort(key=lambda t: t[1], reverse=True)
	for i in range(len(check)):
		if ranked[i][0] != check[i]:
			valid = False
			break

	if valid:
		decrypted = []
		for i in range(len(name)):
			if name[i] == '-':
				decrypted.append(' ')
			else:
				decrypted.append(chr((ord(name[i]) - ord('a') + int(sector)) % 26 + ord('a')))
		decrypted = ''.join(decrypted)

		if 'north' in decrypted:
			print(''.join(decrypted) + ':', sector)

input()
