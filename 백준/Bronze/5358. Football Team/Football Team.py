while True:
    try:
        n = input()
        m = ""
        for c in n:
            if(c == "i"):
                m += "e"
            elif(c == "e"):
                m += "i"
            elif(c == "I"):
                m += "E"
            elif(c == "E"):
                m += "I"
            else:
                m += c
        print(m)
    except:
        exit()