file = open("day8_digits_input.txt")
lines = file.readlines()

result = 0

for i in range(len(lines)) :
    line = lines[i].strip().split("|")
    output = line[1].split(" ")
    
    for j in range(len(output)) :
        length = len(output[j])
        if length == 2 or length == 3 or length == 4 or length == 7 :
            result = result + 1

print(result)
