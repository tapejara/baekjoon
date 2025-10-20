list1 = [0 for _ in range(10)]
for _ in range(5):
    i = int(input())
    list1[i] += 1
for i in range(10):
    if(list1[i] % 2 == 1):
        print(i)