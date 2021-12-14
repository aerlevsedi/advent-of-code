# dla kazdej liczby sposrod wylosowanych w bingo spradzamy w kazdym kwadracie 
# czy taka liczba wystapila jesli tak, to podmieniamy ja na -1
# nastepnie sprawdzamy w kazdym kwadracie czy w ktorejs kolumnie albo wierszu 
# jest juz trafionych 5 liczb, czyli pol ustawionych na -1
# jesli tak to obliczamy sume pozostalych w kwadracie liczb
# i zapisujemy liczbe dla ktorej padlo bingo
# jako wynik zwracamy iloczyn sumy i zapisanej liczby

file = open("day4_bingo_input.txt")
lines = file.readlines()

numbers = lines[0].split(",")

for i in range(len(numbers)) :
    numbers[i] = int(numbers[i])

squares = []

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
        row = lines[i+j].split()
        for k in range(len(row)) :
            row[k] = int(row[k])
        square.append(row)

    squares.append(square)

for number in numbers :
    for square in squares :
        for row in square :
            for i in range(5) :
                if row[i] == number :
                    row[i] = -1

    for square in squares :
        for row in square :
            bingosInRow = 0
            for item in row :
                if item == -1 :
                    bingosInRow += 1
            if bingosInRow == 5 :
                break
            
        for i in range(5) :
            bingosInColumn = 0
            for row in square :
                if row[i] == -1 :
                    bingosInColumn += 1
            if bingosInColumn == 5:
                break

        if bingosInRow == 5 or bingosInColumn == 5:
            for row in square :
                for item in row :
                    if item != -1 :
                        sum += item

            toMult = number
            finish = True
            break

    if finish :
        break
    
print(sum*toMult)
