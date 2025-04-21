list1 = []
for i in range(2024, 100001, 2024):
    list1.append(i)
n = int(input())
if(n in list1):
    print("Yes")
else:
    print("No")