import re

bots = dict()
instructions = []

for line in open('input.txt', 'r'):
    line = line.strip()
    if line.startswith('value'):
        m = re.match('value (\d+) goes to bot (\d+)', line)
        (value, bot) = [int(x) for x in m.group(1, 2)]
        if bot not in bots:
            bots[bot] = []
        bots[bot].append(value)
    else:
        instructions.append(line)

while instructions:
    line = instructions.pop(0)
    m = re.match('bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)', line)
    (sender, lrId, hrId) = [int(x) for x in m.group(1, 3, 5)]
    (lrType, hrType) = m.group(2, 4)
    
    if sender not in bots or len(bots[sender]) < 2:
        instructions.append(line)
        continue

    if 61 in bots[sender] and 17 in bots[sender]:
        print(sender)
        break

    bots[sender].sort()
    if lrType == 'bot':
        if lrId not in bots:
            bots[lrId] = []
        bots[lrId].append(bots[sender][0])
    if hrType == 'bot':
        if hrId not in bots:
            bots[hrId] = []
        bots[hrId].append(bots[sender][1])

input()
