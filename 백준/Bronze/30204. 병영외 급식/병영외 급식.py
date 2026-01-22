n, x = map(int,input().split())
list1 = list(map(int,input().split()))
total = sum(list1)
if(total % x == 0):
    print(1)
else:
    print(0)