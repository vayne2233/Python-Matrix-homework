from sys import *


def judge(unit):
    while len(unit) != n:
        print("輸入的元素不夠")
        unit = list(map(int, stdin.readline().split()))
    return unit


print("行列式計算")
print("------------------")
print("計算2階還是3階矩陣")

n = int(stdin.readline())

array = [[] for i in range(n)]

if n == 2:
    print("請輸入2階矩陣")
    for i in range(2):
        element = list(map(float, stdin.readline().split()))
        element = judge(element)
        array[i] = element

    det = array[0][0] * array[1][1] - array[0][1] * array[1][0]

    print("行列式 = {}".format(round(det, 4)))

elif n == 3:
    print("請輸入3階矩陣")
    for i in range(n):
        element = list(map(float, stdin.readline().split()))
        element = judge(element)
        array[i] = element

    det = array[0][0] * (array[1][1] * array[2][2] - array[1][2] * array[2][1]) - \
        (array[0][1] * (array[1][0] * array[2][2] - array[1][2] * array[2][0])) + \
        (array[0][2] * (array[1][0] * array[2][1] - array[1][1] * array[2][0]))

    print("行列式 = {}".format(round(det, 4)))

else:
    print("無法計算")
