n = int(input())
def function1(arr1, arr2):
    arr0 = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                arr0[i][j] = (arr0[i][j] + (arr1[i][k] * arr2[k][j])) % (10 ** 9 + 7)
    return arr0
def function2(a, arr1):
    if(a == 1):
        return arr1
    elif(a % 2 == 0):
        b = function2(a // 2, arr1)
        c = function1(b, b)
        return c
    elif(a % 2 == 1):
        b = function2((a - 1) // 2, arr1)
        c1 = function1(b, b)
        c2 = function1(c1, arr1)
        return c2
print(function2(n, [[1, 1], [1, 0]])[0][1])