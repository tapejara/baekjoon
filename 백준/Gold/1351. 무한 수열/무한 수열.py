n, p, q = map(int,input().split())
dic = dict({n : 1})
while True:
    if(len(dic) == 1 and 0 in dic):
        break
    temp = dict({})
    for key in dic:
        a = dic[key]
        if(0 in temp and key == 0):
            temp[key] += a
            continue
        elif(0 not in temp and key == 0):
            temp[key] = a
            continue
        if(key // p in temp):
            temp[key // p] += a
        else:
            temp[key // p] = a
        if(key // q in temp):
            temp[key // q] += a
        else:
            temp[key // q] = a
    dic = temp.copy()
print(dic[0])