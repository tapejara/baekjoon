from decimal import Decimal
dec = Decimal
n, l, w, h = map(int,input().split())
a = min(l, w, h)
min, max = 0, a
while min <= max:
    mid = (min + max) / 2
    if((l // mid) * (w // mid) * (h // mid) < n):
        max = dec(str(mid)) - dec(str(10**(-9)))
    else:
        min = dec(str(mid)) + dec(str(10**(-9)))
print(max)