from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
connection = []
while True:
    a = tuple(map(int,input().split()))
    if(a[0] == -1 and a[1] == -1):
        break
    connection.append(a)
point = [[0 for _  in range(n)] for _ in range(n)]
for i in range(n):
    point[i][i] = -1
    for element in connection:
        if(element[0] == i + 1):
            point[i][element[1] - 1] = 1
        elif(element[1] == i + 1):
            point[i][element[0] - 1] = 1
    for j in range(n):
        q = deque([])
        if(point[i][j] == 0):
            q.append((j + 1, 0))
        while q:
            num, count = q.popleft()
            if(point[i][num - 1] == -1):
                point[i][j] = count
                break
            for element in connection:
                if(element[0] == num):
                    q.append((element[1], count + 1))
                elif(element[1] == num):
                    q.append((element[0], count + 1))
result = []
for i in range(n):
    result.append(max(point[i]))
print(min(result), result.count(min(result)))
for i in range(n):
    if(result[i] == min(result)):
        print(i + 1, end = " ")