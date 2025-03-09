import sys, math
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
def function(n, l):
    if(n == 1):
        return l[0]
    temp1 = math.gcd(*l[:n//2]) + function(n - n//2, l[n//2:])
    temp2 = math.gcd(*l[n//2:]) + function(n//2, l[:n//2])
    return max(temp1, temp2)    
print(function(n, list1))