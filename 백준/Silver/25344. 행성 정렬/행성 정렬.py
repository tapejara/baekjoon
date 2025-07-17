import math
n = int(input())
list1 = list(map(int,input().split()))
answer = 1
for i in range(n - 2):
    answer = math.lcm(answer,list1[i])
print(answer)