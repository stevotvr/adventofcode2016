from collections import Counter

columns = 8
characters = []
for i in range(columns):
    characters.append([])

for line in open('input.txt', 'r'):
    line = line.strip()
    for i in range(columns):
        characters[i].append(line[i])

print(''.join([Counter(c).most_common(1)[0][0] for c in characters]))
input()
