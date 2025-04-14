import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
for i in range(n - 1):
    list1[i] %= 10**9 + 7
a = sum(list1) % (10**9 + 7)
list2 = []
temp = 0
for i in range(n - 2, 0, -1):
    temp = (list1[i - 1] * ((temp % (10**9 + 7) + list1[i]) % (10**9 + 7))) % (10**9 + 7)
    list2.append(temp)
b = sum(list2) % (10**9 + 7)
print((a % (10**9 + 7) + b % (10**9 + 7)) % (10**9 + 7))