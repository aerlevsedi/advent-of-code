import statistics

file = open("day7_crabs_input.txt")
line = file.readline()

crabs = line.split(",")

for i in range(len(crabs)) :
    crabs[i] = int(crabs[i])

bestPosition = statistics.median(crabs)
align = 0 

for crab in crabs :
    dist = abs(bestPosition - crab)
    align += dist

print(align)

