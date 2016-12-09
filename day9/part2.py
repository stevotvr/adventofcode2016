def getLength(data):
    length = i = 0
    while i < len(data):
        if data[i] == '(':
            markerEnd = data.find(')', i)
            (chars, repeat) = [int(x) for x in data[i + 1:markerEnd].split('x')]
            length += getLength(data[markerEnd + 1:markerEnd + chars + 1]) * repeat
            i = markerEnd + chars
        else:
            length += 1
        i += 1
    return length

compressed = open('input.txt', 'r').readline().strip()
print(getLength(compressed))
input()
