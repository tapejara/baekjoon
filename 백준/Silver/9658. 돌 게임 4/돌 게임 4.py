n = int(input())
game = ["CY", "SK", "CY", "SK"]
for i in range(4, n):
    if(game[i - 4] == "CY"):
        game.append("SK")
    elif(game[i - 3] == "CY"):
        game.append("SK")
    elif(game[i - 1] == "CY"):
        game.append("SK")
    else:
        game.append("CY")
print(game[n - 1])