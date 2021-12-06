file = open("day6_lanternfish_input.txt")
line = file.readline()

numbers = line.split(",")

fishes = [0 for i in range(9)]

for i in range(len(numbers)) :
    timer = int(numbers[i])
    fishes[timer] += 1

for d in range(80) :
    tmp = fishes[0]

    for i in range(8) :
        fishes[i] = fishes[i+1]

    fishes[6] += tmp
    fishes[8] = tmp

sum = 0

for count in fishes :
    sum += count

print(sum)