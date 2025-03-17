import sys
input = sys.stdin.readline
def function(m):
    if(m == 1):
        return "-"
    else:
        return function(m // 3) + " " * (m // 3) +function(m // 3)
while True:
    try:
        n = int(input())
        print(function(3 ** n))
    except:
        break