import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    list1 = list(map(int,input().split()))
    a = True
    for i in range(len(list1)):
        if(i < 4):
            if(list1[i] != i):
                a = False
                break
        else:
            if(list1[i] != list1[i - 1] + list1[i - 2] + list1[i - 3] + list1[i - 4]):
                a = False
                break
    if(a == True):
        print("NAUTILUS")
    else:
        print("SNAIL")