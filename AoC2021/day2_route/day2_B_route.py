file = open("task2_route_input.txt")

lines = file.readlines()
horizontal = 0
depth = 0
aim = 0

for line in lines :
    direction = line.split(" ")

    if direction[0] == "down" :
        aim += int(direction[1])
    elif direction[0] == "up" :
        aim -= int(direction[1])
    elif direction[0] == "forward" :
        horizontal += int(direction[1])
        depth += aim * int(direction[1])

res = horizontal * depth
print(res)