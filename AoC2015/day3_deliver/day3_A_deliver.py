file = open("day3_deliver_input.txt")

line = file.readline()
horizontal = 0
vertical = 0
presents = 1

horizontals = [0]
verticals = [0]

for direction in line :
    
    if direction == '<' :
        horizontal += 1
    elif direction == '>' :
        horizontal -= 1
    elif direction == '^' :
        vertical += 1
    elif direction == 'v' :
        vertical -= 1

    notVisited = True
    for i in range(len(horizontals)) :
        if horizontals[i] == horizontal and verticals[i] == vertical :
            notVisited = False
    
    if notVisited :
        presents += 1
        horizontals.append(horizontal)
        verticals.append(vertical)

print(presents)