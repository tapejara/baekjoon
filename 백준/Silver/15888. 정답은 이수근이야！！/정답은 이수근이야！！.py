a, b, c = map(int,input().split())
x1 = ((b ** 2 - 4 * a * c) ** 0.5 - b) / (2 * a)
x2 = (-1 * ((b ** 2 - 4 * a * c) ** 0.5 + b)) / (2 * a)
if(b ** 2 - 4 * a * c < 0):
    print("둘다틀렸근")
else:
    if(x1 == x2):
        print("둘다틀렸근")
    elif(x1 != int(x1) or x2 != int(x2)):
        print("둘다틀렸근")
    else:
        temp = 2
        flag1 = False
        flag2 = False
        while max(x1, x2) >= temp:
            if(temp == x1):
                flag1 = True
            if(temp == x2):
                flag2 = True
            temp *= 2
        if(flag1 == True and flag2 == True):
            print("이수근")
        else:
            print("정수근")