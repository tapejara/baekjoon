n, k = map(int,input().split())
table = list(input())
for _ in range(k):
    table.append(0)
count = 0
for i in range(len(table)):
    if(table[i] == "H"):
        for j in range(1,k + 1):
            if(table[i + j] == "P"):
                count += 1
                table[i + j] = 0
                break
    elif(table[i] == "P"):
        for j in range(1,k + 1):
            if(table[i + j] == "H"):
                count += 1
                table[i + j] = 0
                break
print(count)