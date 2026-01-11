import sys
input = sys.stdin.readline
t = int(input())
list1 = [[] for _ in range(10)]
for i in range(10):
    for j in range(1,10):
        if(i ** j % 10 not in list1[i]):
            list1[i].append(i ** j % 10)
list1[1].append(1)
list1[0][0] = 10
for _ in range(t):
    a, b = map(int,input().split())
    a %= 10
    b %= len(list1[a])
    b -= 1
    print(list1[a][b])