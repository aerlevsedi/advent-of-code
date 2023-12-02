import statistics
import math

file = open("day7_crabs_input.txt")
line = file.readline()

crabs = line.split(",")

for i in range(len(crabs)) :
    crabs[i] = int(crabs[i])

print(sum(crabs))
bestPosition = math.floor(sum(crabs) / len(crabs))
align = 0 
print(bestPosition)

for crab in crabs :
    dist = abs(bestPosition - crab)
    align += ((1 + dist) * dist) / 2

print(align)

