file = open("day3_input.txt")
lines = file.readlines()

length = len(lines[0]) - 1

gamma = [0 for i in range(length)]
epsilon = [0 for i in range(length)]

for i in range(length) :
    numberOfZeros = 0
    numberOfOnes = 0
    for line in lines :
        if line[i] == '0' :
            numberOfZeros += 1
        elif line[i] == '1' :
            numberOfOnes += 1
    
    if numberOfZeros < numberOfOnes :
        gamma[i] = 1
        epsilon[i] = 0
    else :
        gamma[i] = 0
        epsilon[i] = 1

gammaDecimal = 0
epsilonDecimal = 0

pow = 1

for i in range(length-1, -1, -1) :
    gammaDecimal += gamma[i] * pow
    epsilonDecimal += epsilon[i] * pow
    pow = pow * 2

res = gammaDecimal * epsilonDecimal

print(res)