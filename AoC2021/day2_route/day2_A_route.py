# ustawiamy poczatkowo glebokosc i polozenie na 0
# wczytujemy wejscie, idziemy po kolejnych liniach i sprawdzamy,
# czy pierwsze słowo to 
# down -> wtedy zwiekszamy glebokosc o odana wartosc
# up -> zmniejszamy glebokosc o podana wartosc
# forward -> zwiekszamy polozenie w poziomie o podana wartosc
# na koniec obliczamy iloczyn glebokosc * polozenie w poziomie

file = open("day2_route_input.txt")

lines = file.readlines()
horizontal = 0
depth = 0

for line in lines :
    direction = line.split(" ")

    if direction[0] == "down" :
        depth += int(direction[1])
    elif direction[0] == "up" :
        depth -= int(direction[1])
    elif direction[0] == "forward" :
        horizontal += int(direction[1])

res = horizontal * depth
print(res)