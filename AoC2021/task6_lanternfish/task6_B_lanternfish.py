file = open("task6_input.txt")
line = file.readline()

numbers = line.split(",")

fishes = [0 for i in range(9)]

for i in range(len(numbers)) :
    timer = int(numbers[i])
    fishes[timer] += 1

print(fishes)

for d in range(256) :
    print("przed", fishes)
    tmp = fishes[0]

    for i in range(8) :
        fishes[i] = fishes[i+1]

    fishes[6] += tmp
    fishes[8] = tmp

    print("po", fishes, "\n")

sum = 0

for count in fishes :
    sum += count

print(sum)