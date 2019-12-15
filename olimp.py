f = open('input.txt', 'r')
value = int(f.readline())
f.close()

lst = []
k = 0

for i in range(2, value + 1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0

ou = open('output.txt', 'w')
ou.write(str(len(lst)))
ou.close()
