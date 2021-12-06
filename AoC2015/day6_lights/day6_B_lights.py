file = open("day6_lights_input.txt")
lines = file.readlines()

lights = [[0 for i in range(1000)] for j in range(1000)]

for line in lines :
    command = line.split(" ")

    if len(command) == 5 :
        opt = command[1]
        firstPair = command[2].split(",")
        secondPair = command[4].split(",")

        if opt == "on" :
            for i in range(int(firstPair[0]), int(secondPair[0])+1) :
                for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                    lights[i][j] += 1
        elif opt == "off" :
            for i in range(int(firstPair[0]), int(secondPair[0])+1) :
                for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                    lights[i][j] = max(0, lights[i][j]-1)

    elif len(command) == 4 :
        firstPair = command[1].split(",")
        secondPair = command[3].split(",")

        for i in range(int(firstPair[0]), int(secondPair[0])+1) :
            for j in range(int(firstPair[1]), int(secondPair[1])+1) :
                lights[i][j] += 2

numberOfLightsOn = 0

for i in range(1000) :
    for j in range(1000) :
        numberOfLightsOn += lights[i][j]

print(numberOfLightsOn)