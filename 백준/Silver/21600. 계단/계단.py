import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
count = 0
list2 = []
for i in range(n):
    if(list1[i] > count):
        count += 1
        list2.append(count)
    elif(list1[i] <= count):
        count = list1[i]
        list2.append(count)
print(max(list2))