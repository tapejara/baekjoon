n, p, q, x, y = map(int,input().split())
dict1 = {}
def function(c):
    if(c <= 0):
        return 1
    elif(c in dict1):
        return dict1[c]
    else:
        dict1[c] = function(c // p - x) + function(c // q - y) 
        return dict1[c]
print(function(n))