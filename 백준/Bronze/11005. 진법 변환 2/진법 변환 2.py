a, b = map(int,input().split())

c = ""

while True:

    if(a >= b):

        if(a % b > 9):

            c += str(chr((a % b)+55))

        else:

            c += str(a % b)

        a = a // b

    elif(a < b):

        if(a % b > 9):

            c += str(chr((a % b)+55))

            break

        else:

            c += str(a % b)

            break

print(c[::-1])