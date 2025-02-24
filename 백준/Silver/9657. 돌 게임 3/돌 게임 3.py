n = int(input())
list1 = ["SK", "CY", "SK", "SK"]
for i in range(4, n):
    if(list1[i - 4] == "CY"):
        list1.append("SK")
    elif(list1[i - 3] == "CY"):
        list1.append("SK")
    elif(list1[i - 1] == "CY"):
        list1.append("SK")
    else:
        list1.append("CY")
print(list1[n - 1])