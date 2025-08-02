n, m = map(int,input().split())
list1 = [input() for _ in range(3 * n)]
list2 = [[list1[i][j] for j in range(8 * m)] for i in range(3 * n) ]
for i in range(1, n * 3, 3):
    for j in range(m):
        temp = list1[i][j * 8: j * 8 + 8]
        q = temp.strip(".")
        if(int(q[0]) + int(q[2]) == int(q[4:])):
            list2[i][j * 8] = "*"
            list2[i][j * 8 + len(q) + 1] = "*"
            for k in range(i - 1, i + 2, 2):
                for l in range(j * 8 + 1, j * 8 + len(q) + 1):
                    list2[k][l] = "*"
        else:
            list2[i - 1][j * 8 + 3] = "/"
            list2[i][j * 8 + 2] = "/"
            list2[i + 1][j * 8 + 1] = "/"
for i in range(3 * n):
    for j in range(8 * m):
        if(j == 8 * m - 1):
            print(list2[i][j])
        else:
            print(list2[i][j], end= "")