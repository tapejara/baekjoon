n = int(input())
a = 1
for i in range(1,n + 1):
    a *= i
a //= 60 * 60 * 24 * 7
print(a)