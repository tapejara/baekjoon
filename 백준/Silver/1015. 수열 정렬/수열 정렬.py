n = int(input())
a = list(map(int,input().split()))
p = [0 for _ in range(n)]
temp = a.copy()
temp.sort()
for i in range(n):
    p[i] = temp.index(a[i])
    temp[temp.index(a[i])] = 0
for num in p:
    print(num, end = " ")