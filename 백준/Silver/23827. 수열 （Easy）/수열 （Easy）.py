import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
mod = 10 ** 9 + 7
temp = sum(list1)
answer = 0
for i in range(n):
    temp -= list1[i]
    answer += (temp * list1[i]) % mod
print(answer % mod)