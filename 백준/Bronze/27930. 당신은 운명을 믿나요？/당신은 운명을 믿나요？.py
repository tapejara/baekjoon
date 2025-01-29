s = input()
count_y = 0
count_k = 0
for c in s:
    if(count_y == 0 and c == "Y"):
        count_y += 1
    if(count_y == 1 and c == "O"):
        count_y += 1
    if(count_y == 2 and c == "N"):
        count_y += 1
    if(count_y == 3 and c == "S"):
        count_y += 1
    if(count_y == 4 and c == "E"):
        count_y += 1
    if(count_y == 5 and c == "I"):
        print("YONSEI")
        break
    if(count_k == 0 and c == "K"):
        count_k += 1
    if(count_k == 1 and c == "O"):
        count_k += 1
    if(count_k == 2 and c == "R"):
        count_k += 1
    if(count_k == 3 and c == "E"):
        count_k += 1
    if(count_k == 4 and c == "A"):
        print("KOREA")
        break