import sys
input = sys.stdin.readline
n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(list1[i])):
        if(0 < j < len(list1[i]) - 1):
            list1[i][j] += max(list1[i - 1][j - 1], list1[i - 1][j])
        elif(j == 0):
            list1[i][j] += list1[i - 1][j] 
        elif(j == len(list1[i]) - 1):
            list1[i][j] += list1[i - 1][j - 1]
print(max(list1[-1]))