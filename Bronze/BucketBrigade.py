f = open('buckets.in')
file = open('buckets.out', 'a')

def inBetween(b, l, r):
    if b > l:
        if r < b and r > l:
            return True
        else:
            return False
    if l > b:
        if r < l and r > b:
            return True
        else:
            return False


for x in range(10):
    yes = f.readline()
    for i in range(10):
        if yes[i] == 'B':
            b = [x, i]
        if yes[i] == 'R':
            r = [x, i]
        if yes[i] == 'L':
            l = [x, i]


if b[0] == l[0]:
    if b[0] == r[0] and inBetween(b[1], l[1], r[1]):
        file.write(str(abs(b[1] - l[1]) + 1))
    else:
        file.write(str(abs(b[1] - l[1]) - 1))
if b[1] == l[1]:
    if b[1] == r[1] and inBetween(b[0], l[0], r[0]):
        file.write(str(abs(b[0] - l[0]) + 1))
    else:
        file.write(str(abs(b[0] - l[0]) - 1))

if b[1] != l[1] and b[0] != l[0]:
    file.write(str(abs(b[0] - l[0]) + abs(b[1] - l[1]) - 1))


f = open('buckets.out', 'r')
file_contents = f.read()
print (file_contents)

f.close()

"""

"""
