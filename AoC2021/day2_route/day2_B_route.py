# ustawiamy poczatkowo cel, glebokosc i polozenie na 0
# wczytujemy wejscie, idziemy po kolejnych liniach i sprawdzamy,
# czy pierwsze słowo to 
# down -> wtedy zwiekszamy cel (aim) o odana wartosc
# up -> zmniejszamy cel (aim) o podana wartosc
# forward -> zwiekszamy polozenie w poziomie o podana wartosc
#         -> obliczamy glebokosc jako iloczyn aim * wartosc
# na koniec obliczamy iloczyn glebokosc * polozenie w poziomie

file = open("day2_route_input.txt")

lines = file.readlines()
horizontal = 0
depth = 0
aim = 0

for line in lines :
    direction = line.split(" ")

    if direction[0] == "down" :
        aim += int(direction[1])
    elif direction[0] == "up" :
        aim -= int(direction[1])
    elif direction[0] == "forward" :
        horizontal += int(direction[1])
        depth += aim * int(direction[1])

res = horizontal * depth
print(res)