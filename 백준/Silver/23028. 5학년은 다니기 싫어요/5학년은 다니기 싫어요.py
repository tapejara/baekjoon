import sys
input = sys.stdin.readline
n, a, b = map(int,input().split())
list1 = []
count_x = a
count_y = b - a
for i in range(1,11):
    x, y = map(int,input().split())
    if(n + i > 8):
        continue
    count_x += x * 3
    if(6 - x <= y):
        count_y += (6 - x) * 3
    elif(6 - x > y):
        count_y += y * 3
if(count_x >= 66 and count_x + count_y >= 130):
    print("Nice")
else:
    print("Nae ga wae")