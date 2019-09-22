f = open('square.in')
file = open('square.out', 'a')

firstIn = f.readline().split()
firstIn = [int(x) for x in firstIn]

secondIn = f.readline().split()
secondIn = [int(x) for x in secondIn]

firstCoords = [[0 for x in range(2)] for a in range(2)]
secondCoords = [[0 for x in range(2)] for a in range(2)]

count = 0
for x in range(2):
    for a in range(2):
        firstCoords[x][a] = firstIn[count]
        secondCoords[x][a] = secondIn[count]
        count+=1

print(firstCoords)
print(secondCoords)

xPair1 = abs(secondCoords[0][1] - firstCoords[1][1])
yPair1 = abs(secondCoords[0][0] - firstCoords[1][0])
xPair2 = abs(secondCoords[1][0] - firstCoords[0][0])
yPair2 = abs(secondCoords[1][1] - firstCoords[0][1])

file.write(str(max(xPair1, xPair2, yPair1, yPair2) ** 2))

f = open('square.out', 'r')
file_contents = f.read()
print(file_contents)


"""
if xPair1 >= xPair2:
    final1 = xPair1
if xPair2 >= xPair1:
    final1 = xPair2

if yPair1 >= yPair2:
    final2 = yPair1
if yPair2 >= yPair1:
    final2 = yPair2

if final1 >= final2:
    file.write(str(final1 ** 2))
else:
    file.write(str(final2 ** 2))
"""