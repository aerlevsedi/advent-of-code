file = open("day2_paper_input.txt")
lines = file.readlines()

paper = 0

for line in lines :
    dimensions = line.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print(paper)
        
    