a,b,c,d = map(int,input().split()) 
list1 = [a, b, c - a, d - b]
print(min(list1))