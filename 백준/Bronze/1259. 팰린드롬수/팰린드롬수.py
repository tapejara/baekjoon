while True:
    n = input().strip()
    if(n == "0"):
        break
    palindrome = True
    for i in range(len(n) // 2):
        if(n[i] == n[len(n) - 1 - i]):
            continue
        else:
            palindrome = False
    if(palindrome == True):
        print("yes")
    else:
        print("no")