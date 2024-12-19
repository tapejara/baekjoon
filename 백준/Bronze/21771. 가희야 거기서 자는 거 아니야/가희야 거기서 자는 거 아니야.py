r, c = map(int,input().split())
rg, cg, rp, cp= map(int,input().split())
a = 0
for _ in range(r):
    b = input()
    for i in range(c):
        if(b[i] == "P"):
            a += 1
if(a != rp * cp):
    print(1)
else:
    print(0)