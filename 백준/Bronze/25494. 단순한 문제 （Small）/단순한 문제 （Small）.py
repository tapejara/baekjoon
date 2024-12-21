a = int(input())
for i in range(a):
    b, c, d = map(int,input().split())
    e = 0
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            for l in range(1, d + 1):
                if(j % k == k % l == l % j):
                    e += 1
    print(e)