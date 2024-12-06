while True:
    a = input()
    if(a == "#"):
        break
    print(a.count("A") + a.count("a") + a.count("E") + a.count("e") + a.count("I") + a.count("i") + a.count("O") + a.count("o") +a.count("U") + a.count("u"))