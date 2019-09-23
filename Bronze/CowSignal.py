f = open('cowsignal.in')
file = open('cowsignal.out', 'a')


def checkInBounds(list1, r, c):
    if r < 0 or r > len(list1) - 1:
        return False
    if c < 0 or c > len(list1[0]) - 1:
        return False

    return True


def fillNoMistakeYes(list1, r, c, val, multi):
    if checkInBounds(list1, r + (multi - 1), c + (multi - 1)):
        for x in range(r, r + multi):
            for a in range(c, c + multi):
                list1[x][a] = val

    return list1


firstIn = f.readline().split()
multi = int(firstIn[2])
expand = [[0 for x in range(int(firstIn[1]) * int(firstIn[2]))] for a in range(int(firstIn[0]) * int(firstIn[2]))]

for x in range(int(firstIn[0])):
    string = f.readline()
    for a in range(int(firstIn[1])):
        expand[x * multi][a * multi] = string[a]


for x in range(int(firstIn[0])):
    for a in range(int(firstIn[1])):
        expand = fillNoMistakeYes(expand, x * multi, a * multi, expand[x * multi][a * multi], multi)

for x in range(len(expand)):
    for a in range(len(expand[0])):
        file.write(str(expand[x][a]))
    file.write('\n')



f = open('cowsignal.out', 'r')
file_contents = f.read()
print(file_contents)
