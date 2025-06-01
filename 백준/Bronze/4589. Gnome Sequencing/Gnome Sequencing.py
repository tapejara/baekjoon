n = int(input())
print("Gnomes:")
for _ in range(n):
    list1 = list(map(int,input().split()))
    list2 = list1.copy()
    list3 = list1.copy()
    list2.sort()
    list3.sort(reverse = True)
    a = True
    b = True
    for i in range(3):
        if(list1[i] != list2[i]):
            a = False
    for i in range(3):
        if(list1[i] != list3[i]):
            b = False
    if(a == True or b == True):
        print("Ordered")
    else:
        print("Unordered")