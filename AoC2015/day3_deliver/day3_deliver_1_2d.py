file = open("task3_deliver_input.txt")

line = file.readline()
horizontal = 0
vertical = 0
presents = 0

horizontals = [0]
verticals = [0]

maxHorizontal = 0
minHorizontal = 0

maxVertical = 0
minVertical = 0

for direction in line :
    
    if direction == '<' :
        horizontal += 1
    elif direction == '>' :
        horizontal -= 1
    elif direction == '^' :
        vertical += 1
    elif direction == 'v' :
        vertical -= 1

    horizontals.append(horizontal)
    verticals.append(vertical)
    
    minHorizontal = min(minHorizontal, horizontal)
    maxHorizontal = max(maxHorizontal, horizontal)

    minVertical = min(minVertical, vertical)
    maxVertical = max(maxVertical, vertical)

minHorizontal *= -1
minVertical *= -1

maxHorizontal += minHorizontal
maxVertical += minVertical

for i in range(len(horizontals)) :
    horizontals[i] += minHorizontal

for i in range(len(verticals)) :
    verticals[i] += minVertical

arr = [[0 for i in range(maxHorizontal + 1)] for j in range(maxVertical + 1)]

for i in range(len(horizontals)) :
    if arr[verticals[i]][horizontals[i]] == 0 :
        presents += 1
    arr[verticals[i]][horizontals[i]] += 1

print(presents)