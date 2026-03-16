import sys
input = sys.stdin.readline
list1 = [1, 1]
for i in range(1,10001):
    list1.append(list1[-1] + list1[-2])
t = int(input())
for i in range(1, t + 1):
    p , q = map(int,input().split())
    print(f"Case #{i}: {list1[p - 1] % q}")