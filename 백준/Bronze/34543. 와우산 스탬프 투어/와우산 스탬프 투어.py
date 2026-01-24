n = int(input())
w = int(input())
total = n * 10
if(n >= 3):
    total += 20
if(n >= 5):
    total += 50
if(w > 1000):
    total -= 15
if(total < 0):
    print(0)
else:
    print(total)