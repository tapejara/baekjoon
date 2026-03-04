list1 = ["063", "010", "093", "079", "106", "103", "119", "011", "127", "107"]
while True:
    n = input()
    if(n == "BYE"):
        exit()
    a, b = n.strip("=").split("+")
    x = ""
    y = ""
    temp1 = ""
    temp2 = ""
    for i in range(len(a)):
        temp1 += a[i]
        if(len(temp1) == 3):
            x += str(list1.index(temp1))
            temp1 = ""
    for i in range(len(b)):
        temp2 += b[i]
        if(len(temp2) == 3):
            y += str(list1.index(temp2))
            temp2 = ""
    z = str(int(x) + int(y))
    answer = ""
    for i in range(len(z)):
        answer += list1[int(z[i])]
    print(n + answer)