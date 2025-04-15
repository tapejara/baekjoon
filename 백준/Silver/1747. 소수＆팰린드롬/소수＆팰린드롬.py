n = int(input())
list1 = [0 for _ in range(0,1003002)]
list1[0] = 1
list1[1] = 1
prime = []
for i in range(2,1001):
    if(list1[i] == 0):
        for j in range(i + i, 1003002, i):
            list1[j] = 1
    else:
        continue
for i in range(0,1003002):
    if(list1[i] == 0):
        prime.append(i)
for element in prime:
    if(element >= n):
        palindrome = True
        c = str(element)
        for i in range(len(c) // 2):
            if(c[i] == c[len(c) - 1 - i]):
                continue
            else:
                palindrome = False
        if(palindrome == True):
            print(element)
            exit()