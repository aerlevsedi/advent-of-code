file = open("task5_niceStrings_input.txt")
lines = file.readlines()

vowels = ['a', 'e', 'i', 'o', 'u']
exceptions = ["ab", "cd", "pq", "xy"]

numberOfNiceWords = 0

for line in lines :
    firstCond = False
    secondCond = False
    thirdCond = True
    
    numberOfVowels = 0

    for letter in line :
        if letter in vowels :
            numberOfVowels += 1
            
        if numberOfVowels == 3 :
            firstCond = True
            break
    
    if not firstCond :
        continue

    for i in range(0, len(line)-1) :
        pair = line[i] + line[i+1]
        isOk = True
        if pair[0] == pair[1] :
            if i > 0 :
                leftPair = line[i-1] + line[i]
                for j in range(0, len(exceptions)) :
                    if leftPair == exceptions[j] :
                        isOk = False
                        break

            if i < len(line) - 2 :
                rightPair = line[i+1] + line[i+2]
                for j in range(0, len(exceptions)) :
                    if rightPair == exceptions[j] :
                        isOk = False
                        break

        if pair[0] == pair[1] and isOk :
            secondCond = True
            break

    if not secondCond :
        continue
    
    for i in range(0, len(line)-1) :
        pair = line[i] + line[i+1]
        thirdCond = True
        for j in range(0, len(exceptions)) :
            if pair == exceptions[j] :
                thirdCond = False
                break
        
        if not thirdCond :
            break

    if firstCond and secondCond and thirdCond:
        numberOfNiceWords += 1

print(numberOfNiceWords)