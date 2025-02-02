ball = list(map(int,input().split()))
box = 0
minimum1 = min(ball)
box += minimum1
for i in range(3):
    ball[i] -=  minimum1
    box += ball[i] // 3
    ball[i] %= 3
if(sum(ball) >= 3 and 2 in ball):
    box += 2
elif(sum(ball) > 0):
    box += 1
print(box)