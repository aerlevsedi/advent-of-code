# podobnie do pierwszej czesci zadania, 
# z tym ze rozpatrujemy rowniez przejscia po przekatnej
# dlatego nalezy rozpoznac z ktorego punktu do ktorego chcemy sie przemieszczac
# w tablicy i odpowiednio przesuwac indeksy
# wynik ponownie jest liczba pol przez ktore przechodza co najmniej dwie rury
file = open("day5_lines_input.txt")
lines = file.readlines()

board = [[0 for i in range(1000)] for j in range(1000)]

for i in range(len(lines)) :
    line = lines[i].split("->")
    
    firstPair = line[0].split(",")
    x1 = int(firstPair[0])
    y1 = int(firstPair[1])

    secondPair = line[1].split(",")
    x2 = int(secondPair[0])
    y2 = int(secondPair[1])

    if x1==x2 :
        top = min(y1, y2)
        bottom = max(y1, y2)
    
        for a in range(top, bottom+1) :
            board[a][x1] += 1

    elif y1==y2 :
        left = min(x1, x2)
        right = max(x1, x2)
        for a in range(left, right+1) :
            board[y1][a] += 1

    else :
        top = min(y1, y2)
        bottom = max(y1, y2)
        dist = bottom - top

        if x1 < x2 and y1 < y2 :
            for j in range(dist+1) :
                board[y1 + j][x1 + j] += 1

        if x1 < x2 and y1 > y2 :
            for j in range(dist+1) :
                board[y1 - j][x1 + j] += 1
    
        if x1 > x2 and y1 < y2 :
            for j in range(dist+1) :
                board[y1 + j][x1 - j] += 1

        if x1 > x2 and y1 > y2 :
            for j in range(dist+1) :
                board[y1 - j][x1 - j] += 1
        
result = 0

for row in board :
    for item in row :
        if item >= 2 :
            result += 1

print(result)