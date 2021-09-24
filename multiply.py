from sys import *


array1 = []
array2 = []

print("乘法")

print("-------------------")

print("第一個矩陣的列與行: ")
row1, column1 = map(int, stdin.readline().split())
print('第二個矩陣的列與行: ')
row2, column2 = map(int, stdin.readline().split())

if column1 != row2:
    print("兩矩陣不能相乘")
else:
    array3 = [[] for i in range(row1)]

    for i in range(row1):
        for j in range(column2):
            array3[i].append(0)

    while column1 != row2:
        print("第一個矩陣的列與行: ")
        row1, column1 = map(int, stdin.readline().split())
        print('第二個矩陣的列與行: ')
        row2, column2 = map(int, stdin.readline().split())

    print("請輸入第一個矩陣")
    for i in range(row1):
        element = list(map(int, stdin.readline().split()))
        while len(element) != column1:
            print("輸入的元素不夠")
            element = list(map(int, stdin.readline().split()))
        array1.append(element)

    print("請輸入第二個矩陣")
    for i in range(row2):
        element = list(map(int, stdin.readline().split()))
        while len(element) != column2:
            print("輸入的元素不夠")
            element = list(map(int, stdin.readline().split()))
        array2.append(element)

    for i in range(row1):
        for j in range(column2):
            for x in range(row2):
                array3[i][j] += array1[i][x] * array2[x][j]

    print("Answer:")
    for i in array3:
        print(" ".join([str(x) for x in i]))
