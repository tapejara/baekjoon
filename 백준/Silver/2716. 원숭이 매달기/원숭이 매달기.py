import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    list1 = list(input().strip())
    count = 0
    max_point = 0
    for i in range(len(list1)):
        if(list1[i] == "["):
            count += 1
        elif(list1[i] == "]"):
            count -= 1
        max_point = max(max_point, count)
    print(2 ** max_point)