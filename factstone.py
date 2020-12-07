from sys import stdin
import math

while True:
    x = int(stdin.readline())

    if x == 0:
        break

    x = (x-1960)//10+2
    m = pow(2,x)
    i=1
    while m>0:
        m -= math.log(i,2)
        i +=1
    print(i-2)