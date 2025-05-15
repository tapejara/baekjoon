import sys
input = sys.stdin.readline
n = int(input())
temp = [tuple(map(int,input().split())) for _ in range(n)]
temp.sort()
butter = []
for i in range(1,n):
    butter.append((abs(temp[i][0] - temp[i - 1][0] - 1), temp[i - 1][1] // 2, temp[i][1] // 2))
time = []
for i in range(n - 1):
    if(butter[i][0] >= butter[i][1] + butter[i][2]):
        continue
    else:
        if(butter[i][1] <= butter[i][0] // 2 or butter[i][2] <= butter[i][0] // 2):
            time.append(butter[i][0] - min(butter[i][1], butter[i][2]))
        else:
            time.append(butter[i][0] // 2)
if(len(time) == 0):
    print("forever")
else:
    print(min(time))