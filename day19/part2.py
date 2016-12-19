inp = 3004953

class Elf:
    def __init__(self, num):
        self.num = num
        self.prev = None
        self.next = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

elves = list(map(Elf, range(1, inp + 1)))
for i in range(inp):
    elves[i].prev = elves[(i - 1) % inp]
    elves[i].next = elves[(i + 1) % inp]

count, current, across = inp, elves[0], elves[inp // 2]
while current != across:
    across.remove()
    across = across.next
    if count % 2 == 1:
        across = across.next
    count -= 1
    current = current.next

print(current.num)
input()
