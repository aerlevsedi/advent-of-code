file = open("task3_diagnostic_input.txt")
lines = file.readlines()

length = len(lines[0]) - 1

gamma = [0 for i in range(length)]
epsilon = [0 for i in range(length)]

oxygen = lines
co2 = lines

for i in range(length) :
    newOxygen = []
    newCO2 = []

    numberOfZerosInOxygen = 0
    numberOfOnesInOxygen = 0

    for line in oxygen :
        if line[i] == '0' :
            numberOfZerosInOxygen += 1
        elif line[i] == '1' :
            numberOfOnesInOxygen += 1
    
    if numberOfZerosInOxygen <= numberOfOnesInOxygen :
        for line in oxygen :
            if line[i] == '1' :
                newOxygen.append(line)
    else :
        for line in oxygen :
            if line[i] == '0' :
                newOxygen.append(line)

    oxygen = newOxygen
    if len(oxygen) == 1:
        break

for i in range(length) :
    newOxygen = []
    newCO2 = []

    numberOfZerosInCO2 = 0
    numberOfOnesInCO2 = 0
    
    for line in co2 :
        if line[i] == '0' :
            numberOfZerosInCO2 += 1
        elif line[i] == '1' :
            numberOfOnesInCO2 += 1

    if numberOfZerosInCO2 > numberOfOnesInCO2 :
        for line in co2 :
            if line[i] == '1' :
                newCO2.append(line)
    else :
        for line in co2 :
            if line[i] == '0' :
                newCO2.append(line)
    
    co2 = newCO2

    if len(co2) == 1 :
        break

oxygen = oxygen[0]
co2 = co2[0]

oxygenDecimal = 0
co2Decimal = 0

pow = 1

for i in range(length-1, -1, -1) :
    oxygenDecimal += int(oxygen[i]) * pow
    co2Decimal += int(co2[i]) * pow
    pow = pow * 2

res = oxygenDecimal * co2Decimal

print(res)