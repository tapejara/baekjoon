a, b = map(int,input().split())
totalX = 0
totalY = 0
for i in range(a):
    x, y= map(int,input().split())
    totalX += x
    totalY += y
c = totalY - b * a
if(totalX == 0):
    print("EZPZ")
else:
    c2 = abs(c)
    x2 = abs(totalX)
    while x2 != 0:
        [c2,x2] = [x2, c2 % x2]
    if(abs(totalX // c2) == 1):
        print(c//totalX)
    elif(c/totalX > 0):
        print(abs(c)//c2, "/" , abs(totalX)//c2, sep= "")
    elif(c == 0):
        print(0)
    else:
        print("-", abs(c)//c2, "/" , abs(totalX)//c2, sep= "")