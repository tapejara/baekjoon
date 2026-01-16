t = int(input())
n = list(map(int,input().split()))
list1 = [0] * 80001
for i in range(1,80001):
    if(i / 3 == i // 3 or i / 7 == i // 7):
        list1[i] = list1[i - 1] + i
    else:
        list1[i] = list1[i - 1]
for i in n:
    print(list1[i])