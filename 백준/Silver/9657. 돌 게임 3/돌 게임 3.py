n = int(input())
list1 = [0, 1, 2, 1, 1, 3]
for i in range(6, n + 1):
    if(list1[i - 4] % 2 == 0):
        list1.append(list1[i - 4] + list1[4])
    elif(list1[i - 3] % 2 == 0):
        list1.append(list1[i - 3] + list1[3])
    else:
        list1.append(list1[i - 1] + list1[1])
if(list1[n] % 2 > 0):
    print("SK")
else:
    print("CY")