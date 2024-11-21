a = int(input())
for i in range(a):
    b = int(input())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    while True:
        if(b >= 25):
            b -= 25
            quarter += 1
        elif(b >= 10):
            b -= 10
            dime += 1
        elif(b >= 5):
            b -= 5
            nickel += 1
        elif(b >= 1):
            b -= 1
            penny += 1
        else:
            break
    print(quarter, dime, nickel, penny)