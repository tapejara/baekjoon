t = int(input())
for i in range(t):
    n = int(input())
    list1 = list(map(int,input().split()))
    list2 = list1[:]
    a = 0
    while True:
        b = 0
        a += 1
        for element in list1:
            b += element
        if(b > n):
            print(a)
            break
        for i in range(6):
            if(i < 5):
                list2[i] += list1[i + 1] + list1[i - 1] + list1[i - 3]
            else:
                list2[i] += list1[0] + list1[i - 1] + list1[i - 3]
        list1 = list2[:]