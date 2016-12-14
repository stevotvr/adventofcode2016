from hashlib import md5
import re

inp = b'zpqevtbw'

def getHash(index):
    m = md5()
    m.update(inp)
    m.update(bytes(str(index), 'utf-8'))
    return m.hexdigest()

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
