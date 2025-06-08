n = int(input())
for _ in range(n):
    l = ""
    c = ""
    str = input()
    for element in str:
        if(l != element):
            c += element
            l = element
    print(c)