list1 = [int(input()) for _ in range(4)]
if((list1[0] == 8 or list1[0] == 9) and (list1[1] == list1[2]) and (list1[3] == 8 or list1[3] == 9)):
    print("ignore")
else:
    print("answer")