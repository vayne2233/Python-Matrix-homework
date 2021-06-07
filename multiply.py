from sys import *
from time import *

array1 = []
array2 = []

print("第一個矩陣的行與列: ")
row1, column1 = map(int, stdin.readline().split())
print('第二個矩陣的行與列: ')
row2, column2 = map(int, stdin.readline().split())

array3 = [[] for i in range(row1)]

for i in range(row1):
    for j in range(column2):
        array3[i].append(0)

while column1 != row2:
    print("第一個矩陣的行與列: ")
    row1, column1 = map(int, stdin.readline().split())
    print('第二個矩陣的行與列: ')
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


print("Result: ")
for i in array3:
    print(" ".join([str(x) for x in i]))

sleep(10)
