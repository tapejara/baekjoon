t = int(input())
for i in range(t):
    a = int(input())
    b = 0
    list1 = [1,2]
    while list1[-1] + list1[-2] <= a:
        list1.append(list1[-1] + list1[-2])
    list2 = []
    for j in range(len(list1) -1,-1,-1):
        if(list1[j] <= a):
            a -= list1[j]
            list2.append(1)
        else:
            list2.append(0)
    list2.pop()
    list3 = list2[::-1]
    for j in range(len(list3)):
        if(list3[j] == 1):
            b += list1[j]
    print(b)