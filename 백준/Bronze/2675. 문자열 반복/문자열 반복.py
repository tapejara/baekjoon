a = int(input())
for _ in range(a):
    b,c = map(str,input().split())
    string = ""
    for element in c:
        for i in range(int(b)):
             string += element
    print(string)    