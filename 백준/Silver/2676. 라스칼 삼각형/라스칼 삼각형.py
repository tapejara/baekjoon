import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    list1 = [1, n]
    k = n - 1
    for i in range(2, n // 2 + 1):
        k -= 2
        list1.append(list1[-1] + k)
    if(m > n // 2):
        print(list1[n - m])
    else:
        print(list1[m])