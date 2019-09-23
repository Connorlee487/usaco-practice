f = open('square.in')
file = open('square.out', 'a')

# You can reduce your code to 1 line
firstIn = [int(x) for x in f.readline().split()]
secondIn = [int(x) for x in f.readline().split()]

# Since you already know the input by size, why do you need a for loop?
# You can access them directly through the array
firstCoords = [[firstIn[0], firstIn[1]], [firstIn[2], firstIn[3]]]
secondCoords = [[secondIn[0], secondIn[1]], [secondIn[2], secondIn[3]]]

#count = 0
#for x in range(2):
#    for a in range(2):
#        firstCoords[x][a] = firstIn[count]
#        secondCoords[x][a] = secondIn[count]
#        count+=1

#print(firstCoords)
#print(secondCoords)

# Your understanding of the question is correct, but your implementation is complex.
# To cover the two squares which are non-overlapping,
# We first find the the minimum x axis and maximum y axis of the two rectangles,
# represent by firstCoords [[1,1], [3,3]] and secondCoords [[5,5], [7,7]]
#
#                                     [7,7]
#
#                            [5,5]
#
#              [3,3]
#
#    [1,1]
#
#  minimumCoords = [[1,1], ]
#

minimumCoords = [
                    [
                    min(firstCoords[0][0], secondCoords[0][0]),
                    min(firstCoords[0][1], secondCoords[0][1])],
                    [
                     max(firstCoords[1][0], secondCoords[1][0]),
                     max(firstCoords[1][1], secondCoords[1][1])]
                ]

# Minimum square is just the maximum length * maximum length
maximumSide = max(
    (minimumCoords[1][0] - minimumCoords[0][0]),
    (minimumCoords[1][1] - minimumCoords[0][1]))

#xPair1 = abs(secondCoords[0][1] - firstCoords[1][1])
#yPair1 = abs(secondCoords[0][0] - firstCoords[1][0])
#xPair2 = abs(secondCoords[1][0] - firstCoords[0][0])
#yPair2 = abs(secondCoords[1][1] - firstCoords[0][1])

#file.write(str(max(xPair1, xPair2, yPair1, yPair2) ** 2))

f = open('square.out', 'r')
file_contents = f.read()
print(maximumSide * maximumSide)
file.write(str(maximumSide * maximumSide))


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