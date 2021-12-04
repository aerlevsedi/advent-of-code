file = open("task4_input.txt")
lines = file.readlines()

numbersStrings = lines[0].split(",")

numbers = []

for nS in numbersStrings :
    numbers.append(int(nS))

squares = []
newSquares = []

finish = False

sum = 0
toMult = 0

for i in range (2, 1000, 6) :
    if i >= len(lines) :
        break
    if len(lines[i]) == 1 :
        continue

    square = []
    
    for j in range(5) :
        rowStrings = lines[i+j].split()
        row = []
        for item in rowStrings :
            row.append(int(item))
        square.append(row)

    squares.append(square)

#print(squares)

for number in numbers :
    for square in squares :
        for row in square :
            for i in range(5) :
                if row[i] == number :
                    row[i] = -1

    bingosInRow = 0
    bingosInColumn = 0
    for square in squares :
        for row in square :
            bingosInRow = 0
            for item in row :
                if item == -1 :
                    bingosInRow += 1
            if bingosInRow == 5 :
                print("Row")
                break
            
        for i in range(5) :
            bingosInColumn = 0
            for row in square :
                if row[i] == -1 :
                    bingosInColumn += 1
            if bingosInColumn == 5:
                print("Column")
                print(square)
                break
        
        print("KUPA")
        print(bingosInColumn)
        print(bingosInRow)

        if bingosInRow == 5 or bingosInColumn == 5:
            print("HALO")
            newSquares = []
            for s in squares :
                print(s)
                if s != square :
                    print(s)
                    newSquares.append(s)
            squares = newSquares
            break

    print(len(squares))
    print(len(newSquares))


    if len(squares) == 1:
        toMult = number
        for row in squares[0] :
            for item in row :
                if item != -1 :
                    sum += item

        break
    
print(sum*toMult)



