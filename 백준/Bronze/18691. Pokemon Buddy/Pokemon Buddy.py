n = int(input())
list1 = [0, 1, 3, 5]
for _ in range(n):
    g, c, e = map(int,input().split())
    if(e >= c):
        print(list1[g] * (e - c))
    else:
        print(0)