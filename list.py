
colors = []
files = ["red.txt", "orange.txt", "brown.txt", "yellow.txt", "green.txt", "blue.txt", "purple.txt", "pink.txt", "white.txt", "gray.txt", "black.txt"]
for j in files:
    f = open(j, "r")
    lines = f.readlines()
    div = []
    for i in lines:
        if i!="\n":
            color = []
            pos = i.index("#")
            color.append(i[0:pos-1])
            color.append(i[pos:len(i)-1])
            div.append(color)

    colors.append(div)

print(colors)


