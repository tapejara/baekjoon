a, b = input().split()
a1 = ""; b1 = ""
a2 = ""; b2 = ""
for num in a:
    if(num == "5" or num  == "6"):
        a1 += "5"
        a2 += "6"
    else:
        a1 += num
        a2 += num
for num in b:
    if(num == "5" or num  == "6"):
        b1 += "5"
        b2 += "6"
    else:
        b1 += num
        b2 += num
print(int(a1) + int(b1), int(a2) + int(b2))