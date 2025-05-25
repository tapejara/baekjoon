list1 = []
answer = -1
for i in range(31623):
    list1.append(i ** 2)
n, m = map(int,input().split())
board = [[i for i in input()] for _ in range(n)]
list2 = []
for i in range(-n + 1, n):
    for j in range(-m + 1, m):
        list2.append((j,i))
for i in range(n):
    for j in range(m):
        for a,b in list2:
            x = j
            y = i
            temp = board[i][j]
            if(int(temp) in list1):
                answer = max(int(temp), answer)
            for k in range(max(n,m) - 1):
                if(-1 < x + a < m and -1 < y + b < n):
                    x += a
                    y += b
                    temp += board[y][x]
                    if(int(temp) in list1):
                        answer = max(int(temp), answer)
                else:
                    continue
print(answer)