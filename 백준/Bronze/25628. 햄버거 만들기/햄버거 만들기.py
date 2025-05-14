a, b = map(int,input().split())
count = 0
while a >= 2 and b >= 1:
    a -= 2
    b -= 1
    count += 1
print(count)