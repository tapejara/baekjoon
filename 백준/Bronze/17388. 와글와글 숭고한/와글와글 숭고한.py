
list1 = list(map(int,input().split()))
if(sum(list1) >= 100):
    print("OK")
elif(list1.index(min(list1)) == 0):
    print("Soongsil")
elif(list1.index(min(list1)) == 1):
    print("Korea")
elif(list1.index(min(list1)) == 2):
    print("Hanyang")