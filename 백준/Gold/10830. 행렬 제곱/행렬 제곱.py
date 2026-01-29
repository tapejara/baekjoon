n, b = map(int,input().split())
list1 = []
for _ in range(n):
    temp1 = list(map(int,input().split()))
    temp2 = []
    for i in range(n):
        temp2.append(temp1[i] % 1000)
    list1.append(temp2)
def function(x,y):
    if(x == 1):
        return y
    elif(x % 2 == 0):
        a = function(x // 2, y)
        b = []
        for i in range(n):
            temp = []
            for j in range(n):
                z = 0
                for k in range(n):
                    z = (z % 1000 + ((a[i][k] % 1000) * (a[k][j] % 1000) % 1000)) % 1000
                temp.append(z)
            b.append(temp)
        return b
    elif(x % 2 == 1):
        a = function((x - 1) // 2, y)
        b = []
        c = []
        for i in range(n):
            temp = []
            for j in range(n):
                z = 0
                for k in range(n):
                    z = (z % 1000 + ((a[i][k] % 1000) * (a[k][j] % 1000) % 1000)) % 1000
                temp.append(z)
            b.append(temp)
        for i in range(n):
            temp = []
            for j in range(n):
                z = 0
                for k in range(n):
                    z = (z % 1000 + ((b[i][k] % 1000) * (y[k][j] % 1000) % 1000)) % 1000
                temp.append(z)
            c.append(temp)
        return c
list2 = function(b, list1)
for i in range(n):
    for j in range(n):
        print(list2[i][j], end = " ")
    print()