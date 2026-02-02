import sys
input = sys.stdin.readline
def function1(a, arr1):
    if(a == 1):
        return arr1
    elif(a % 2 == 0):
        b = function1(a // 2, arr1)
        c = function2(b, b)
        return c
    elif(a % 2 == 1):
        b = function1((a - 1) // 2, arr1)
        c1 = function2(b, b)
        c2 = function2(c1, arr1)
        return c2
def function2(arr1, arr2):
    arr0 = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                arr0[i][j] = (arr0[i][j] + (arr1[i][k] * arr2[k][j])) % 10000
    return arr0
while True:
    n = int(input())
    if(n == -1):
        break
    elif(n == 0):
        print(0)
    else:
        print(function1(n, [[1, 1], [1, 0]])[0][1])