file = open("day6_lights_input.txt")
lines = file.readlines()

lights = [[False for i in range(1000)] for j in range(1000)]

for line in lines :
    command = line.split(" ")

    if len(command) == 5 :
        opt = command[1]
        firstPair = command[2].split(",")
        secondPair = command[4].split(",")

        if opt == "on" :
            for i in range(int(firstPair[0]), int(secondPair[0])+1) :
                for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                    lights[i][j] = True
        elif opt == "off" :
            for i in range(int(firstPair[0]), int(secondPair[0])+1) :
                for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                    lights[i][j] = False

    elif len(command) == 4 :
        firstPair = command[1].split(",")
        secondPair = command[3].split(",")

        for i in range(int(firstPair[0]), int(secondPair[0])+1) :
            for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                lights[i][j] = not lights[i][j]

numberOfLightsOn = 0

for i in range(1000) :
    for j in range(1000) :
        if lights[i][j] == True :
            numberOfLightsOn += 1

print(numberOfLightsOn)