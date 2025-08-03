n = int(input())
list1 = [0 for _ in range(35)]
list2 = list(map(str,input().split()))
for i in range(n):
    if(list2[i][1] == "m"):
        list1[int(list2[i][0])] += 1
    elif(list2[i][1] == "p"):
        list1[int(list2[i][0]) + 9] += 1
    elif(list2[i][1] == "s"):
        list1[int(list2[i][0]) + 18] += 1
    elif(list2[i][1] == "z"):
        list1[int(list2[i][0]) + 27] += 1
    if(5 in list1):
        print(i + 1) 
        exit()
print(0)