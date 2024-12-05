list1 = list(map(int,input().split()))
if(sum(list1) - max(list1) <= max(list1)):
    print((sum(list1) - max(list1)) * 2 - 1)
else:
    print(sum(list1))