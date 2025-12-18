n = int(input())
list1 = [int(input()) for _ in range(n)]
if(list1[1] - list1[0] == list1[2] - list1[1]):
    print(list1[-1] + (list1[1] - list1[0]))
else:
    print(list1[-1] * (list1[1] // list1[0]))