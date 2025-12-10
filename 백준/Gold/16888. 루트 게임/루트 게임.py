import sys
input = sys.stdin.readline
list1 = ["cubelover" for _ in range(10 ** 6 + 1)]
list2 = [i ** 2 for i in range(1, 1001)]
for i in range(1, 10**6 + 1):
    for j in list2:
        if(j > i):
            break
        if(list1[i - j] == "cubelover"):
            list1[i] = "koosaga"
            break
        
t = int(input())
for _ in range(t):
    n = int(input())
    print(list1[n])