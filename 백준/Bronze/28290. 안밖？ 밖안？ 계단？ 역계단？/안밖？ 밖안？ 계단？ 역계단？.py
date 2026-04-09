s = input()
list1 = ["fdsajkl;", "jkl;fdsa", "asdf;lkj", ";lkjasdf", "asdfjkl;", ";lkjfdsa"]
if(s not in list1):
    print("molu")
elif(list1.index(s) == 0 or list1.index(s) == 1):
    print("in-out")
elif(list1.index(s) == 2 or list1.index(s) == 3):
    print("out-in")
elif(list1.index(s) == 4):
    print("stairs")
elif(list1.index(s) == 5):
    print("reverse")