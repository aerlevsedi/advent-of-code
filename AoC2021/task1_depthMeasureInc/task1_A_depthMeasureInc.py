file = open("task1_depthMeasureInc_input.txt")
lines = file.readlines()

oldDepth = int(lines[0])
depthIncreases = 0

for line in lines :
    newDepth = int(line)    # assuming single integer on each line
    
    if oldDepth < newDepth :
        depthIncreases += 1
        
    oldDepth = newDepth

print(depthIncreases)
        
    