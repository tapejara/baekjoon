list1 = [int(input()) for _ in range(4)]
rising = False
diving = False
constant = False
for i in range(1,4):
    if(list1[i - 1] > list1[i]):
        diving = True
    elif(list1[i - 1] < list1[i]):
        rising = True
    elif(list1[i - 1] == list1[i]):
        constant = True
if(rising == False and diving == False):
    print("Fish At Constant Depth")
elif(rising == True and diving == False and constant == False):
    print("Fish Rising")
elif(rising == False and diving == True and constant == False):
    print("Fish Diving")
else:
    print("No Fish")