from sys import stdin

e, f, c = stdin.readline().split()
e = int(e)
f = int(f)
c = int(c)

drinks = 0
while(e+f >= c):
    convert = (e+f)//c
    e = convert + (e+f)%c
    f = 0
    drinks += convert

print(drinks)