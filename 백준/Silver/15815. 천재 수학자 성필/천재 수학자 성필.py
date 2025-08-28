n = input()
list1 = []
for i in range(len(n)):
    if(n[i] !=  "+" and n[i] != "-" and n[i] != "*" and n[i] != "/"):
        list1.append(int(n[i]))
    else:
        a = list1.pop()
        b = list1.pop()
        if(n[i] == "+"):
            list1.append(a + b)
        elif(n[i] == "-"):
            list1.append(b - a)
        elif(n[i] == "*"):
            list1.append(a * b)
        elif(n[i] == "/"):
            list1.append(b // a)
print(list1[0])