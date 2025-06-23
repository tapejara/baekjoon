import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = list(map(int,input().split()))
    m = int(input())
    list2 = [[0 for _ in range(n)] for _ in range(m + 1)]
    list2[list1[0]][0] = 1
    for i in range(m + 1):
        if(list1[0] > i):
            continue
        for j in range(n):
            if(i - list1[j] > 0):
                list2[i][j] = sum(list2[i - list1[j]][:j + 1:])
            elif(i - list1[j] == 0):
                list2[i][j] = 1
    print(sum(list2[m]))