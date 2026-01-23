n = int(input())
for _ in range(n):
    a, b = input().split()
    orgin = int(a) * int(b)
    c = ""
    for i in range(max(len(a),len(b)) - min(len(a), len(b))):
        c += "1"
    if(len(a) < len(b)):
        a = c + a
    elif(len(b) < len(a)):
        b = c + b
    answer = ""
    for i in range(len(a)):
        answer += str(int(a[i]) * int(b[i]))
    if(orgin == int(answer)):
        print(1)
    else:
        print(0)