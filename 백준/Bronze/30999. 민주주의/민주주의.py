n,m = map(int,input().split())
a = 0
for _ in range(n):
    c = input()
    count = 0
    for i in range(m):
        if(c[i] == "O"):
            count += 1
    if(count > m // 2):
        a += 1
print(a)