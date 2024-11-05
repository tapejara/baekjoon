a = input().split()
list1 = [1, 1, 2, 2, 2, 8]
for i in range(6):
    b = int(list1[i]) - int(a[i])
    print(b,end=' ')