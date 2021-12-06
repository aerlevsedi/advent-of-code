file = open("day3_deliver_input.txt")
line = file.readline()

x = 0
y = 0

coordinates = set((0, 0))

for direction in line :
    if direction == '<' :
        x += 1
    elif direction == '>' :
        x -= 1
    elif direction == '^' :
        y += 1
    elif direction == 'v' :
        y -= 1

    coordinates.add((x, y))

print(len(coordinates))