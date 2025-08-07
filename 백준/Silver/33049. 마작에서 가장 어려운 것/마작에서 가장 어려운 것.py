p3, p4, p0 = map(int,input().split())
count3 = p3 // 3
count4 = p4 // 4
p3 %= 3
p4 %= 4
if(p3 > 0):
    p0 -= 3 - p3
    count3 += 1
if(p4 > 0):
    p0 -= 4 - p4
    count4 += 1
for i in range(4):
    temp = p0
    temp -= 3 * i
    if(temp >= 0 and temp % 4 == 0):
        print(count3 + i, count4 + temp // 4)
        exit()
print(-1)