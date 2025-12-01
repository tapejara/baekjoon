import sys
input = sys.stdin.readline
n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
a = 0
b = 0
for i in range(n):
    for j in range(n):
        if(list1[j][i] == 2):
            a = i % 2
            b = j % 2
if(a != b):
    for i in range(n):
        for j in range(n):
            if(list1[j][i] == 1 and j % 2 != i % 2):
                print("Kiriya")
                exit()
    print("Lena")
if(a == b):
    for i in range(n):
        for j in range(n):
            if(list1[j][i] == 1 and j % 2 == i % 2):
                print("Kiriya")
                exit()
    print("Lena")