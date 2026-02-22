a = int(input())
b = int(input())
if(60 + b < a):
    print((a - (60 + b)) * 3000 + (60 + b) * 1500)
else:
    print(a * 1500)