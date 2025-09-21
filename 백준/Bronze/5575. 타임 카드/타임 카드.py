for i in range(3):
    list1 = list(map(int,input().split()))
    a = list1[0] * 3600 + list1[1] * 60 + list1[2]
    b = list1[3] * 3600 + list1[4] * 60 + list1[5]
    c = b - a
    list2 = []
    list2.append(c // 3600)
    c %= 3600
    list2.append(c // 60)
    c %= 60
    list2.append(c)
    for j in range(2):
        print(list2[j], end = " ")
    print(list2[-1])