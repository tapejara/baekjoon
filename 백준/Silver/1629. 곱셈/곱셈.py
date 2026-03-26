def function(x):
    global a, c
    if(x == 0):
        return 1
    elif(x == 1):
        return a % c
    elif(x % 2 == 0):
        y = function(x // 2)
        return ((y % c) * (y % c)) % c
    elif(x % 2 == 1):
        y = function((x - 1) // 2)
        return ((y % c) * (y % c) * (a % c)) % c
a, b, c = map(int,input().split())
print(function(b))