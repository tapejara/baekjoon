import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [(-1, 0) for _ in range(n + 1)]
for i in range(m):
    c, x, h = map(int,input().split())
    list1[x] = (c, h)
point = [0, 0]
for x in range( 1, n + 1):
    c, h = list1[x]
    if(c == 0):
        point[0] += 1
        if(point[1] - 1 <= h):
            point[1] = h + 1
        else:
            point[1] -= 1
    elif(c == 1 and point[1] >= h):
        point[0] += 1
        point[1] -= 1
        if(point[1] >= h):
            print("adios")
            exit()
    elif(x == n and point[1] > h):
        point[0] += 1
        point[1] -= 1
        if(point[0] == x and point[1] == h):
            print("stay")
        else:
            print("adios")
    elif(x == n and point[1] <= h):
        point[0] += 1
        point[1] = h
        if(point[0] == x and point[1] == h):
            print("stay")
        else:
            print("adios")
    else:
        point[0] += 1
        point[1] -= 1