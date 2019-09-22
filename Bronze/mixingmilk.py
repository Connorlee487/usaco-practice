f = open('mixmilk.in')
file = open('mixmilk.out', 'a')

limit = []
milk = []

for x in range(3):
    stage = f.readline().split()
    limit.append(int(stage[0]))
    milk.append(int(stage[1]))

for x in range(3):

    for y in range(3):
        if y != 2:
            if milk[y] + milk[y+1] > limit[y+1]:
                milk[y] = milk[y] + milk[y+1] - limit[y+1]
                milk[y+1] = limit[y+1]
            else:
                milk[y+1] = milk[y] + milk[y+1]
                milk[y] = 0
        else:
            if milk[2] + milk[0] > limit[0]:
                milk[2] = milk[2] + milk[0] - limit[0]
                milk[0] = limit[0]
            else:
                milk[0] = milk[2] + milk[0]
                milk[2] = 0

if milk[0] + milk[1] > limit[1]:
    milk[0] = milk[0] + milk[1] - limit[1]
    milk[1] = limit[1]
else:
    milk[1] = milk[0] + milk[1]
    milk[0] = 0

file.write(str(milk[0]) + '\n')
file.write(str(milk[1]) + '\n')
file.write(str(milk[2]) + '\n')

f = open('mixmilk.out', 'r')
file_contents = f.read()
print(file_contents)
 