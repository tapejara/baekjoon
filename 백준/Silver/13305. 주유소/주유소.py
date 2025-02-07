import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
flag = list2[0]
price = 0 
for i in range(n - 1):
    if(flag >= list2[i]):
        flag = list2[i]
        price += flag * list1[i]
    else:
        price += flag * list1[i]
print(price)