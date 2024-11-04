a = input()
list1 = list(a)
alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV','WXYZ']
count = 0
for i in range(len(list1)):
    for element in alphabet:
        if(element.count(list1[i]) == 1):
            count += 3 + alphabet.index(element)
print(count)