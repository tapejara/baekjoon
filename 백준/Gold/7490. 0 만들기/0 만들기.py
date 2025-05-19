from itertools import product
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = [i for i in range(1,n + 1)]
    calculation = ["+", "-", " "]
    answer = []
    for element in product(calculation, repeat= n - 1):
        c = ""
        for i in range(n):
            if(i == n - 1):
                c += str(list1[i])
            else:
                c += str(list1[i])
                c += element[i]
        list2 = []
        temp = "1"
        for i in range(1, 2 * n - 1):
            if(c[i] == "+"):
                list2.append(int(temp))
                temp = ""
            elif(c[i] == "-"):
                list2.append(int(temp))
                temp = "-"
            elif(c[i] == " "):
                continue
            elif(i == 2 * n - 2):
                temp += c[i]
                list2.append(int(temp))
            else:
                temp += c[i]
        result = sum(list2)
        if(result == 0):
            answer.append(c)
    answer.sort()
    for i in range(len(answer)):
        if(i == len(answer) - 1):
            print(answer[i], "\n")
        else:
            print(answer[i])