n = int(input())
factorial_list = ["1"]
b = 1
for i in range(1,21):
    b *= i
    factorial_list.append(b)
    if(b > n):
        break
for i in range(len(factorial_list)):
    for element in factorial_list:
        if(element == n):
            print("YES")
            exit()
        copy_element = element
        for j in range(i,len(factorial_list)):
            if(copy_element != factorial_list[j]):
                element = int(element) + int(factorial_list[j])
                if(element == n):
                    print("YES")
                    exit()
print("NO")