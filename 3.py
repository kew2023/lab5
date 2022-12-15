file = open('C:/Users/эльдо750/Desktop/Проги/Алгомы/5 лаба/3.txt','r')
t = file.readlines()
arr = [
    [i for i in l if i != '\n'] for l in t
]

flag = 0
dict1 = {}
visiting = set()
def build_graf(start):
    global visiting
    global dict1
    global arr
    global flag
    visiting.add(start)
    i,j = map(int,start.split())
    
    if (i == 0 or j == 0) and flag == 1: return 
    if (i == 14 or j == 14) and flag == 1: return 
    flag = 1
    dict1[start] = []
    if j != 0:
        i2 = i
        j2 = j+1
        if arr[i2][j2] == '0' and '1':
            next = f'{i2} {j2}' 
            if next not in visiting:
                dict1[start].append(next)
                build_graf(next)
        i2 = i
        j2 = j-1
        if arr[i2][j2] == '0' and '2':
            next = f'{i2} {j2}'
            if next not in visiting:
                dict1[start].append(next)
                build_graf(next)

        i2 = i+1
        j2 = j
        if arr[i2][j2] == '0' and '3':
            next = f'{i2} {j2}'
            if next not in visiting:
                dict1[start].append(next)
                build_graf(next)

        i2 = i-1
        j2 = j
        if arr[i2][j2] == '0' and '4':
            next = f'{i2} {j2}'
            if next not in visiting:
                dict1[start].append(next)
                build_graf(next)
    else:
        i2 = i
        j2 = j+1
        if arr[i2][j2] == '0':
            next = f'{i2} {j2}'
            if next not in visiting:
                dict1[start].append(next)
                build_graf(next)


    '''if j == 0:
        dict1[start] = []
        if arr[i+1][j] == 0:
            next = f'{i+1} {j}'
            if next not in visiting: 
                dict1[start].append(next)
                build_graf(next)
        if arr[i-1][j] == 0:
            next = f'{i-1} {j}'
            if next not in visiting: 
                dict1[start].append(next)
                build_graf(next)'''

start = '7 0'
end = '7 14'
build_graf(start)
dict2 = {}
dict1_items = dict1.items()
for item in dict1_items:
    for value in item[1]:
        dict2[value] = item[0]
print(dict2)
currect = end

way = []

while True:
    i,j = map(int, currect.split())
    arr[i][j] = 'x'
    way.append(currect)
    if currect == start: break
    currect = dict2[currect]
print(*way[::-1], sep = '\n')
print(*arr,sep = '\n')
