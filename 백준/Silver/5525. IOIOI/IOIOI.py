n = int(input())
m = int(input())
s = list(input())
c = s[0]
answer = 0
for i in range(1,m):
    if(c[-1] == "O" and s[i] == "I"):
        c += s[i]
        if(len(c) >= 2 * n + 1):
            answer += 1
    elif(c[-1] == "I" and s[i] == "O"):
        c += s[i]
    else:
        c = s[i]
print(answer)