list1 = [1 for _ in range(1001)]
prime = []
for i in range(2,1001):
    if(list1[i] == 1):
        prime.append(i)
        for j in range(i,1001,i):
            list1[j] = 0
a, b = map(int,input().split())
c, d = map(int,input().split())
yt = 0
yj = 0
count = 0
for num in prime:
    if(a <= num and num <= b):
        yt += 1
    if(c <= num and num <= d):
        yj += 1
    if(a <= num and num <= b and c <= num and num <= d):
        count += 1
yt -= count
yj -= count
if(count % 2 == 1):
    yt += 1
if(yt > yj):
    print("yt")
else:
    print("yj")