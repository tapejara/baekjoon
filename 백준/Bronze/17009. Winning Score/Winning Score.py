a_score = 0
b_score = 0
for i in range(3, 0, -1):
    s = int(input())
    a_score += i * s
for i in range(3, 0, -1):
    s = int(input())
    b_score += i * s
if(a_score > b_score):
    print("A")
elif(b_score > a_score):
    print("B")
else:
    print("T")