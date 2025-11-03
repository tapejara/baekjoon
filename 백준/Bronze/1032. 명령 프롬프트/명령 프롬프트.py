n = int(input())
list1 = [i for i in input()]
for _ in range(n - 1):
    s = input()
    for i in range(len(list1)):
        if(s[i] != list1[i]):
            list1[i] = "?"
for i in range(len(list1)):
    print(list1[i], end = "")