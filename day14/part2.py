from hashlib import md5
import re

inp = 'zpqevtbw'

def getHash(index):
    hash = inp + str(index)
    for _ in range(2017):
        m = md5()
        m.update(bytes(hash, 'utf-8'))
        hash = m.hexdigest()
    return hash

def getChar(hash):
    match = re.search(r'(\w)\1\1', hash)
    if match:
        return match.group(1)

index = 0
hashes = []
count = 0
while True:
    hash = getHash(index)
    nextChar = getChar(hash)
    if nextChar:
        for i, c in hashes.copy():
            if index - i > 1000:
                hashes.remove((i, c))
                continue
            if c * 5 in hash:
                count += 1
                if count == 64:
                    print(i)
                    input()
                    exit()
                hashes.remove((i, c))
        hashes.append((index, nextChar))
    index += 1
