file = open("task1_floors_input.txt")

floor = 0
pos = 0
while True :
    sign = file.read(1)
    if sign == '(' :
        floor += 1
    elif sign == ')' :
        floor -= 1
    elif not sign :
        break
    
    pos += 1
    if floor == -1 :
        break

print(pos)
        
    