from sys import *


array = []

print("加法")

print("------------------")

print("請輸入矩陣的行與列")
row, column = map(int, stdin.readline().split())

print("-----")

for i in range(row):
    array.append(list(map(int, stdin.readline().split())))

print("-----")

for i in range(row):
    enter = list(map(int, stdin.readline().split()))
    for j in range(column):
        array[i][j] += enter[j]

print("Answer:")
for i in array:
    print(" ".join(str(x) for x in i))