n = int(input())
list1 = [0, 1, 2, 1]
for i in range(4, n + 1):
    if(i % 3 == 0):
        list1.append(list1[i - 3] + list1[3]) 
    elif(i % 3 == 1):
        list1.append(list1[i - 1] + list1[1])
    elif(i % 3 == 2):
        list1.append(list1[i - 1] + list1[1])
if(list1[n] % 2 == 1):
    print("SK")
else:
    print("CY")