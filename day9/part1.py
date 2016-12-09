compressed = open('input.txt', 'r').readline().strip()
uncompressed = []

i = 0
while i < len(compressed):
    if compressed[i] == '(':
        markerEnd = compressed.find(')', i)
        (chars, repeat) = [int(c) for c in compressed[i + 1:markerEnd].split('x')]
        uncompressed += compressed[markerEnd + 1:markerEnd + chars + 1] * repeat
        i = markerEnd + chars + 1
    else:
        uncompressed.append(compressed[i])
        i = i + 1

print(len(uncompressed))
input()
