n = int(input())
s = list(input())
if(s.count("(") != s.count(")")):
    print(-1)
    exit()
answer = 1
temp = [s[0]]
for i in range(1,len(s)):
    if(not temp):
        temp.append(s[i])
    elif(temp[-1] == s[i]):
        temp.append(s[i])
        answer = max(answer,len(temp))
    elif(temp[-1] != s[i]):
        temp.pop()
print(answer)