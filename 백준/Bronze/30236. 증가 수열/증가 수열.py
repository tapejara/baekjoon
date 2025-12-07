import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = list(map(int,input().split()))
    answer = 0
    if(list1[0] != 1):
        answer = 1
    else:
        answer = 2
    for i in range(1,n):
        if(list1[i] == answer + 1):
            answer += 2
        else:
            answer += 1
    print(answer)