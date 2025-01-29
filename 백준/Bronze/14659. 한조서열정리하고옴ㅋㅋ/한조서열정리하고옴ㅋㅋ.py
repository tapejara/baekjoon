import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
answer = []
for i in range(n - 1):
    count = 0
    for j in range(i + 1, n):
        if(list1[i] > list1[j]):
            count += 1
        else:
            break
    answer.append(count)
print(max(answer))