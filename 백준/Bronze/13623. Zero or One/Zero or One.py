a, b, c = map(int,input().split())
if(a == b == c):
    print("*")
elif(a == b and a != c):
    print("C")
elif(a == c and a != b):
    print(("B"))
elif(b == c and a != b):
    print("A")