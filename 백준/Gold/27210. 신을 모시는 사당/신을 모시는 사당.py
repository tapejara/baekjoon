import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
count1 = 0
count2 = 0
answer = 0
for i in range(n):
    if(list1[i] == 1):
        count1 += 1
        count2 -= 1
    else:
        count1 -= 1
        count2 += 1
    if(count1 < 0):
        count1 = 0
    if(count2 < 0):
        count2 = 0
    answer = max(count1, count2,  answer)
print(answer)