file = open("day7_crabs_input.txt")
line = file.readline()

crabs = line.split(",")
maksPos = 0

for i in range(len(crabs)) :
    crabs[i] = int(crabs[i])
    maksPos = max(maksPos, crabs[i])

bestAlign = 1000000000

for i in range(maksPos+1) :
    currenAlign = 0
    for j in range(len(crabs)) :
        dist = abs(i - crabs[j])
        currenAlign += dist
        if currenAlign >= bestAlign :
            break

    bestAlign = min(currenAlign, bestAlign)

print(bestAlign)
