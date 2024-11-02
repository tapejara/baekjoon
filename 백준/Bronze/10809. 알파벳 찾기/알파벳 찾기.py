a = str(input())
for i in range(97,123):
    if(a.count(chr(i)) == 0):
        print(-1,end=' ')
    elif(a.count(chr(i)) >= 1):
        print(a.index(chr(i)),end=' ')