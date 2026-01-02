n = int(input())
count = len(str(n))
list1 = [2 ** i for i in range(5)]
for i in range(5):
    if(len(str(n * list1[i])) > count):
        print(i - 1)
        exit()