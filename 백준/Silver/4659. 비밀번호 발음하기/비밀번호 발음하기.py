list1 = ["a","e","i","o","u"]
list2 = ["b","c","d","f","g","h","j","k","l","n","m","p","q","r","s","t","v","w","x","y","z"]
while True:
    a = input()
    if(a == "end"):
        break
    if(not ("a" in a or  "e" in a or "i" in a or "o" in a or"u" in a)):
        print(f"<{a}> is not acceptable.")
        continue
    if(len(a) == 1):
        print(f"<{a}> is acceptable.")
    elif(len(a) == 2):
        if(a[0] == a[1] != "e" and a[0] == a[1] != "o"):
            print(f"<{a}> is not acceptable.")
            break
        else:
            print(f"<{a}> is acceptable.")
    else:
        b = True
        for i in range(2,len(a)):
            if(a[i -2] in list1 and a[i -1] in list1 and a[i] in list1):
                print(f"<{a}> is not acceptable.")
                b = False
                break
            elif(a[i -2] in list2 and a[i -1] in list2 and a[i] in list2):
                print(f"<{a}> is not acceptable.")
                b = False
                break
        if(b == False):
            continue
        for i in range(1,len(a)):
            if(a[i - 1] == a[i] != "e" and a[i - 1] == a[i] != "o"):
                print(f"<{a}> is not acceptable.")
                b = False
                break
            else:
                b = True
        if(b == True):
            print(f"<{a}> is acceptable.")