inp = 3004953

elves = list(range(1, inp + 1))
i = 0
while len(elves) > 1:
    index = (i + int(len(elves) / 2)) % len(elves)
    elves.pop(index)
    if index < i:
        i -= 1
    i = (i + 1) % len(elves)

print(elves[0])
input()
