while True:
    try:
        list1 = list(map(int,input().split()))
        list2 = [list1[:3]]
        for i in range(1, list1[-1] + 1):
            temp = [0] * 3
            temp[2] += list2[i - 1][0] * list1[3]
            temp[1] += list2[i - 1][2] // list1[4]
            temp[0] += list2[i - 1][1] // list1[5]
            list2.append(temp)
        print(list2[-1][0])
    except:
        exit()