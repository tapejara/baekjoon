a = int(input())
total = set()
for _ in range(a):
    b, c = map(int,input().split())
    for i in range(10):
        for j in range(10):
            total.add((b,c))
            c += 1
        b += 1
        c -= 10
print(len(total))