f = open('blocks.in')
file = open('blocks.out', 'a')


def add(list1, final):
    for x in range(len(list1)):
        final[x] += list1[x]

    return final


def compare(list1, list2):
    for x in range(len(list1)):
        if list1[x] < list2[x]:
            list1[x] = list2[x]
    return list1

def countChar(word):
    index = [0 for x in range(26)]
    for x in word:
        index[ord(x) - 97] +=1

    return index



numOfBlocks = int(f.readline())
blocks = [0 for x in range(numOfBlocks)]
indexAns = [0 for x in range(26)]

for x in range(numOfBlocks):
    inn = f.readline().split()
    inn = [str(a) for a in inn]
    blocks[x] = inn


for x in range(numOfBlocks):
    count1 = countChar(blocks[x][0])
    count2 = countChar(blocks[x][1])
    ans = compare(count1, count2)
    indexAns = add(ans, indexAns)

for x in indexAns:
    file.write(str(x) + '\n')


#TAKE MAX OF LETTER COUNT
f = open('blocks.out', 'r')
file_contents = f.read()
print(file_contents)