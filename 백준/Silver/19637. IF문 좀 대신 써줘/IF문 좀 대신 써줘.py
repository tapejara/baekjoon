import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = []
list2 = []
for _ in range(n):
    a, b = input().split()
    if(list1):
        if(list2[-1] < int(b)):
            list1.append(a)
            list2.append(int(b))
    else:
        list1.append(a)
        list2.append(int(b))
list3 = [int(input()) for _ in range(m)]
for element in list3:
    minimum = 0
    maximum = len(list2) - 1
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if(element <= list2[mid]):
            maximum = mid - 1
        else: minimum = mid + 1
    print(list1[maximum +1])