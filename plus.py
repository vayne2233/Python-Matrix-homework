from sys import *
from time import *

array = []

print("請輸入矩陣的行與列")
row, column = map(int, stdin.readline().split())

print("要相加多少矩陣")
quantity = int(stdin.readline())

for j in range(quantity):
    print("請輸入第%d個矩陣" % (j + 1))
    for i in range(row):
        if j == 0:
            ay = list(map(int, stdin.readline().split()))

            while len(ay) != column:
                print("輸入的元素不夠")
                ay = list(map(int, stdin.readline().split()))
            array.append(ay)
        else:
            ay = list(map(int, stdin.readline().split()))

            while len(ay) != column:
                print("輸入的元素不夠")
                ay = list(map(int, stdin.readline().split()))

            for x in range(len(array[i])):
                array[i][x] += ay[x]
                
print("Answer:")
for i in range(len(array)):
    print(array[i])

sleep(10)
