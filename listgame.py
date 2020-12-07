from sys import stdin

n = int(stdin.readline())

factors = 0
factor = 2

while factor**2 <= n:
    if n % factor == 0:
        n = n/factor
        factors += 1
    else:
        factor += 1

print(factors+1)