import math
f = open('input.txt', 'r')

bunny = f.readline()
bunny = bunny.split(' ')
bunny_x = int(bunny[0])
bunny_y = int(bunny[1])

fox = f.readline()
fox = fox.split(' ')
fox_x = int(fox[0])
fox_y = int(fox[1])

n = f.readline()
n = int(n)

for i in range(1, n + 1):
    hole = f.readline()
    hole = hole.split(' ')
    hole_x = int(hole[0])
    hole_y = int(hole[1])

    bunny_h = math.sqrt((hole_x - bunny_x) ** 2 + (hole_y - bunny_y) ** 2)
    fox_h = math.sqrt((hole_x - fox_x) ** 2 + (hole_y - fox_y) ** 2)

    if fox_h // bunny_h >= 2:
        hope = i
        break
    else:
        hope = 'NO'

ou = open('output.txt', 'w')
ou.write(str(hope))
ou.close()
