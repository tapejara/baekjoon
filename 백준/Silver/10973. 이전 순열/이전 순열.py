n = int(input())
list1 = list(map(int,input().split()))
flag = True
for i in range(n - 1, 0, -1):
    if(list1[i] < list1[i - 1]):
        flag = False
        check = list1[i - 1]
        list1[i - 1] = min(list1[i::])
        for j in range(n -1, i - 1, -1):
            if(list1[i - 1] <= list1[j] and check > list1[j]):
                list1[i - 1], list1[j] = list1[j], check
        list2 = list1[:i]
        list3 = list1[i:]
        list3.sort(reverse= True)
        break
if(flag == True):
    print(-1)
else:
    answer = list2 + list3
    for i in range(n):
        print(answer[i], end=" ")