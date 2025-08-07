p3, p4, p0 = map(int,input().split())
count3 = 0
count4 = 0
count3 += p3 // 3
count4 += p4 // 4
p3 %= 3
p4 %= 4
if(p3 > 0):
    p0 -= 3 - p3
    count3 += 1
if(p4 > 0):
    p0 -= 4 - p4
    count4 += 1
if(p0 < 0):
    print(-1)
    exit()
temp = 0
temp += p0 // 4
p0 %= 4
if(p0 == 3):
    print( count3 + 1, count4 + temp)
elif(p0 == 2):
    temp -= 1
    if(temp < 0):
        print(-1)
    else:
        print(count3 + 2, count4 + temp)
elif(p0 == 1):
    temp -= 2
    if(temp < 0):
        print(-1)
    else:
        print(count3 + 3, count4 + temp)
else:
    print(count3, count4 + temp)