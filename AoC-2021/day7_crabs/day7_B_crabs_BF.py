file = open("day7_crabs_input.txt")
line = file.readline()

crabs = line.split(",")
maksPos = 0

for i in range(len(crabs)) :
    crabs[i] = int(crabs[i])
    maksPos = max(maksPos, crabs[i])

bestAlign = 1000000000
pos = -1

for i in range(maksPos+1) :
    currentAlign = 0
    for j in range(len(crabs)) :
        dist = abs(i - crabs[j])
        currentAlign += ((1 + dist) * dist) / 2

    if bestAlign > currentAlign :
        pos = i
    bestAlign = min(currentAlign, bestAlign)

print(pos)
print(bestAlign)
