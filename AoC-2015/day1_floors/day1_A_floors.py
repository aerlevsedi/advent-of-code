file = open("day1_floors_input.txt")

floor = 0

while True :
    sign = file.read(1)
    if sign == '(' :
        floor += 1
    elif sign == ')' :
        floor -= 1
    elif not sign :
        break

print(floor)
        
    