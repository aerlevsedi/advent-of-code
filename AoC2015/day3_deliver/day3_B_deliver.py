file = open("day3_deliver_input.txt")

horizontal = 0
vertical = 0

horizontalRoboSanta = 0
verticalRoboSanta = 0

presents = 1

horizontals = [0]
verticals = [0]

while True:
    direction = file.read(1)
    directionRoboSanta = file.read(1)

    if direction == '<' :
        horizontal += 1
    elif direction == '>' :
        horizontal -= 1
    elif direction == '^' :
        vertical += 1
    elif direction == 'v' :
        vertical -= 1

    if directionRoboSanta == '<' :
        horizontalRoboSanta += 1
    elif directionRoboSanta == '>' :
        horizontalRoboSanta -= 1
    elif directionRoboSanta == '^' :
        verticalRoboSanta += 1
    elif directionRoboSanta == 'v' :
        verticalRoboSanta -= 1
    elif not directionRoboSanta :
        break

    notVisited = True
    for i in range(len(horizontals)) :
        if horizontals[i] == horizontal and verticals[i] == vertical :
            notVisited = False
    
    if notVisited :
        presents += 1
        horizontals.append(horizontal)
        verticals.append(vertical)

    notVisited = True
    for i in range(len(horizontals)) :
        if horizontals[i] == horizontalRoboSanta and verticals[i] == verticalRoboSanta :
            notVisited = False
    
    if notVisited :
        presents += 1
        horizontals.append(horizontalRoboSanta)
        verticals.append(verticalRoboSanta)

print(presents)