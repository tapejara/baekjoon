a = int(input())
b = list(map(int,input().split()))
c = 0
for element in b:
    d = 0
    for i in range(1, element + 1):
        if(element % i == 0):
            d += 1
    if(d == 2):
        c += 1
print(c)