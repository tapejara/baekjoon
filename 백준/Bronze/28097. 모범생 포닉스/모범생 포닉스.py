n = int(input())
list1 = list(map(int,input().split()))
d = sum(list1) + 8 * (n - 1)
print(d // 24, d % 24)
