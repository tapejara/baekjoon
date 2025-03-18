import sys
input = sys.stdin.readline
n = int(input())
square = [list(map(int,input().split())) for _ in range(n)]
def function(x, l):
    if(len(l) == 2):
        a = l[0] + l[1]
        a.sort()
        return a[1]
    else:
        temp = [function(x // 2, [l[i][:x // 2] for i in range(x // 2)]),
                function(x // 2, [l[i][x // 2:] for i in range(x // 2)]),
                function(x // 2, [l[i][:x // 2] for i in range(x // 2, x)]),
                function(x // 2, [l[i][x // 2:] for i in range(x // 2, x)])]
        temp.sort()
        return temp[1]
if(n > 1):
    print(function(n, square))
else:
    print(square[0][0])