a, b = map(int,input().split())
c = max(a,b) - min(a,b)
if(c == 0):
    print(a)
elif(c == 1):
    print(a + b)
elif(c % 2 == 1):
    print((a + b) * (c // 2) + (a + b))
else:
    print((a + b) * (c // 2) + ((a + b) // 2))