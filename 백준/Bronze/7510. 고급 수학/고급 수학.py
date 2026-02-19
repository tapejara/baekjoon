n = int(input())
for i in range(1,n + 1):
    list1 = list(map(int,input().split()))
    list1.sort()
    print(f"Scenario #{i}:")
    if(list1[0] ** 2 + list1[1] ** 2 == list1[2] ** 2):
        print("yes")
    else:
        print("no")
    if(i < n):
        print()