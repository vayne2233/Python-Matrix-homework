from sys import *


def judge(unit):
    while len(unit) != n:
        print("輸入的元素不夠")
        unit = list(map(int, stdin.readline().split()))
    return unit


print("反矩陣計算")
print("------------------")
print("計算2階還是3階矩陣")
n = int(stdin.readline())

array = []

if n == 2:

    print("請輸入2階矩陣")
    for i in range(n):
        element = list(map(int, stdin.readline().split()))
        element = judge(element)
        array.append(element)

    det = array[0][0] * array[1][1] - array[0][1] * array[1][0]

    if det == 0:
        print("此矩陣沒有反矩陣")
    else:
        array[0][0], array[1][1] = round(
            (array[1][1] / det), 4), round((array[0][0] / det), 4)
        array[0][1] = round((array[0][1] / (-1*det)), 4)
        array[1][0] = round((array[1][0] / (-1*det)), 4)

        for i in array:
            print(" ".join([str(x) for x in i]))

elif n == 3:
    print("請輸入3階矩陣")
    for i in range(n):
        element = list(map(int, stdin.readline().split()))
        element = judge(element)
        array.append(element)

    det = array[0][0] * (array[1][1] * array[2][2] - array[1][2] * array[2][1]) - \
        (array[0][1] * (array[1][0] * array[2][2] - array[1][2] * array[2][0])) + \
        (array[0][2] * (array[1][0] * array[2][1] - array[1][1] * array[2][0]))

    if det == 0:
        print("此矩陣沒有反矩陣")
    else:
        a11 = array[0][0]
        a12 = array[0][1]
        a13 = array[0][2]
        a21 = array[1][0]
        a22 = array[1][1]
        a23 = array[1][2]
        a31 = array[2][0]
        a32 = array[2][1]
        a33 = array[2][2]

        array[0][0] = (a22 * a33 - a23 * a32) / det
        array[0][1] = -1 * (a12 * a33 - a32 * a13) / det
        array[0][2] = (a12 * a23 - a22 * a13) / det
        array[1][0] = -1 * (a21 * a33 - a31 * a23) / det
        array[1][1] = (a11 * a33 - a31 * a13) / det
        array[1][2] = -1 * (a11 * a23 - a21 * a13) / det
        array[2][0] = (a21 * a32 - a22 * a31) / det
        array[2][1] = -1 * (a11 * a32 - a31 * a12) / det
        array[2][2] = (a31 * a22 - a21 * a12) / det

        for i in array:
            print(' '.join([str(x) for x in i]))
else:
    print("無法計算")
