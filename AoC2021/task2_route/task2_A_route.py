file = open("task2_route_input.txt")

lines = file.readlines()
horizontal = 0
depth = 0

for line in lines :
    direction = line.split(" ")
    print(direction[0] + "x" + direction[1])
    if direction[0] == "down" :
        depth += int(direction[1])
    elif direction[0] == "up" :
        depth -= int(direction[1])
    elif direction[0] == "forward" :
        horizontal += int(direction[1])

res = horizontal * depth
print(res)