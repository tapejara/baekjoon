n = int(input())
n = 1000 - n 
a = 0
a += n // 500
n %= 500
a += n // 100
n %= 100
a += n // 50
n %= 50
a += n // 10
n %= 10
a += n // 5
n %= 5
a += n
print(a)