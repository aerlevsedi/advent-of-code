file = open("day2_paper_input.txt")
lines = file.readlines()
ribbon = 0

for line in lines :
    dimensions = line.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    minimum = min(l, w, h)
    if l == minimum :
        ribbon += 2 * (l + min(w, h))
    elif w == minimum :
        ribbon += 2 * (w + min(l, h))
    elif h == minimum :
        ribbon += 2 * (h + min(w, l)) 

    ribbon += l*w*h

print(ribbon)
        
    