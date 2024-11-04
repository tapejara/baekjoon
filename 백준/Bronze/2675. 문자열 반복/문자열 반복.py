a = int(input())
for _ in range(a):
    b,c = map(str,input().split())
    string = ""
    for element in c:
        string += element*int(b)
    print(string)