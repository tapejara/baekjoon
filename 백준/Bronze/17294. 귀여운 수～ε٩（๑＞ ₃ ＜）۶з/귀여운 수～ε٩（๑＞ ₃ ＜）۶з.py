a = input()
list1 = []
for i in range(1,len(a)):
    list1.append(int(a[i - 1]) - int(a[i]))
for j in range(1,len(list1)):
    if(not list1[j - 1] == list1[j]):
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        exit()
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")