import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = [list(map(int,input().split())) for _ in range(2)]
    list2 = [[0] * n for _ in range(3)]
    list2[1][0] = list1[0][0]
    list2[2][0] = list1[1][0]
    for i in range(1, n):
        list2[0][i] += max(list2[1][i - 1], list2[2][i - 1])
        list2[1][i] += max(list2[0][i - 1], list2[2][i - 1]) + list1[0][i]
        list2[2][i] += max(list2[0][i - 1], list2[1][i - 1]) + list1[1][i]
    print(max(list2[0][-1], list2[1][-1], list2[2][-1]))