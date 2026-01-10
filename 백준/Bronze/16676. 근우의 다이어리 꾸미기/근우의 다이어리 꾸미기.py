n = input()
if(int(n) == 0):
    print(1)
elif(int(n) < int("1" * len(n))):
    print(len(n) - 1)
else:
    print(len(n))