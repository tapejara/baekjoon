l = int(input())
s = [0] + list(map(int,input().split()))
n = int(input())
s.sort()
if(n in s):
    print(0)
else:
    for i in range(1, l + 1):
        if(s[i - 1] < n < s[i]):
            print((n - s[i - 1]) * (s[i] - n) - 1)