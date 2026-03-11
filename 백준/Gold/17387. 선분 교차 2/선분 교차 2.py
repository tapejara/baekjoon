l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
def function(a,b,x,y,n,m):
    return (a * y + x * m + n * b) - (a * m + x * b + n * y)
a = function(l1[0],l1[1],l1[2],l1[3],l2[0],l2[1]) 
b = function(l1[0],l1[1],l1[2],l1[3],l2[2],l2[3])
c = function(l2[0],l2[1],l2[2],l2[3],l1[0],l1[1]) 
d = function(l2[0],l2[1],l2[2],l2[3],l1[2],l1[3])
point1 = a * b
point2 = c * d
if(point1 < 0 and point2 < 0):
    print(1)
elif(point1 == 0 or point2 == 0):
    if(a == 0 and min(l1[0],l1[2]) <= l2[0] <= max(l1[0],l1[2]) and min(l1[1],l1[3]) <= l2[1] <= max(l1[1],l1[3])):
        print(1)
    elif(b == 0 and min(l1[0],l1[2]) <= l2[2] <= max(l1[0],l1[2]) and min(l1[1],l1[3]) <= l2[3] <= max(l1[1],l1[3])):
        print(1)
    elif(c == 0 and min(l2[0],l2[2]) <= l1[0] <= max(l2[0],l2[2]) and min(l2[1],l2[3]) <= l1[1] <= max(l2[1],l2[3])):
        print(1)
    elif(d == 0 and min(l2[0],l2[2]) <= l1[2] <= max(l2[0],l2[2]) and min(l2[1],l2[3]) <= l1[3] <= max(l2[1],l2[3])):
        print(1)
    else:
        print(0)
else:
    print(0)