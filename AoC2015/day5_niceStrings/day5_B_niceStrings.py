file = open("task5_niceStrings_input.txt")
lines = file.readlines()

numberOfNiceWords = 0

for line in lines :
    firstCond = False
    secondCond = False

    for i in range(0, len(line)-1) :
        pair = line[i] + line[i+1]
        
        for j in range(i+2, len(line)) :
            if j >= len(line)-1 :
                break
            
            newPair = line[j] + line[j+1]
            
            if pair == newPair :
                firstCond = True
                break

        if firstCond :
            break
        
    if not firstCond :
        continue

    for i in range(0, len(line)-2) :
        if line[i] == line[i+2] :
            secondCond = True
            break
    
    if secondCond :
        print(line)
        numberOfNiceWords += 1

print(numberOfNiceWords)