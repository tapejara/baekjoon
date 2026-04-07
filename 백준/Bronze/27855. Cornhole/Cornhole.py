list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
a = list1[0] * 3 + list1[1]
b = list2[0] * 3 + list2[1]
if(a == b):
    print("NO SCORE")
elif(a > b):
    print(1, a - b)
else:
    print(2, b - a)