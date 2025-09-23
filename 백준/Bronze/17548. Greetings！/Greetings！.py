n = input()
count = 0
for element in n:
    if(element == "e"):
        count += 1
print("h", end = "")
for _ in range(count * 2):
    print("e", end = "")
print("y")