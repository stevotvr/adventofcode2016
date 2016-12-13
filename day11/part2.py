from itertools import combinations
import re

elements = {}
def getElement(name):
    if name not in elements:
        elements[name] = len(elements) + 1
    return elements[name]

floors = [[], [], [], []]
index = 0
for line in open('input.txt', 'r'):
    floors[index] += [getElement(e) for e in re.findall('a (\w+)-compatible microchip', line)]
    floors[index] += [-getElement(e) for e in re.findall('a (\w+) generator', line)]
    index += 1
elerium, dilithium = len(elements) + 1, len(elements) + 2
floors[0] += [elerium, -elerium, dilithium, -dilithium]
inputState = (0, tuple([tuple(sorted(x)) for x in floors]))

def isFloorValid(floor):
    if not floor or floor[0] > 0 or floor[-1] < 0:
        return True
    return all(-x in floor for x in floor if x > 0)

stateHistory = set()
def addToHistory(state):
    flattened = ['({}|{})'.format(len([g for g in x if g < 0]), len([m for m in x if m > 0])) for x in state[1]]
    flattened = '{}({})'.format(state[0], ''.join(flattened))
    if flattened in stateHistory:
        return False
    stateHistory.add(flattened)
    return True

addToHistory(inputState)
distances = {inputState: 0}
stack = [inputState]
while stack:
    state = stack.pop(0)
    currentFloor, floors = state
    distance = distances[state]

    if currentFloor == len(floors) - 1 and not any(floors[:-1]):
        print(distance)
        break

    options = list(combinations(floors[currentFloor], 2)) + list(combinations(floors[currentFloor], 1))
    for i in [i for i in (currentFloor - 1, currentFloor + 1) if 0 <= i < len(floors)]:
        for option in options:
            newCurrentFloor = tuple(sorted([x for x in floors[currentFloor] if x not in option]))
            newNextFloor = tuple(sorted(floors[i] + option))
            if isFloorValid(newCurrentFloor) and isFloorValid(newNextFloor):
                newFloors = list(floors)
                newFloors[currentFloor] = newCurrentFloor
                newFloors[i] = newNextFloor
                newState = (i, tuple(newFloors))
                if not addToHistory(newState):
                    continue
                if newState not in distances or distances[newState] > distance + 1:
                    distances[newState] = distance + 1
                    stack.append(newState)

input()
