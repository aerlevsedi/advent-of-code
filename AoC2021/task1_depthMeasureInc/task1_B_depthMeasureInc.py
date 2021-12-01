file = open("task1_depthMeasureInc_input.txt")
lines = file.readlines()

oldDepthSum = int (lines[0]) + int(lines[1]) + int(lines[2])
depthIncreases = 0

index = 2

while index < len(lines) :
    newDepthSum = int(lines[index-2]) + int(lines[index-1]) + int(lines[index])    # assuming single integer on each line
    
    if oldDepthSum < newDepthSum :
        depthIncreases += 1
        
    oldDepthSum = newDepthSum
    index += 1

print(depthIncreases)
        
    