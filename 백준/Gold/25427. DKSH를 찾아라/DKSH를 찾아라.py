n = int(input())
list_n = [c for c in input()]
point = [0,0,0,0]
for i in range(len(list_n)):
    if(list_n[i] == "D"):
        point[0] += 1
    elif(list_n[i] == "K"):
        point[1] += point[0]
    elif(list_n[i] == "S"):
        point[2] += point[1]
    elif(list_n[i] == "H"):
        point[3] += point[2]
print(point[3])
