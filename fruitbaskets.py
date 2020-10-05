from itertools import combinations
from sys import stdin
from functools import reduce
import operator as op

#implementation of combination function
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

n = int(stdin.readline())
fruit = []

for x in stdin.readline().split():
    fruit.append(int(x))

i = 1

total = 0

#all combinations of less than 4 fruits
while i < 4 and i <= n:
    for c in combinations(fruit, i):
        if sum(c) >= 200:
            total += sum(c)
    i += 1

#when it's more than 4 fruits, we know that it's always over 200g
#since each fruit is over 50g
for i in range(4, n + 1):
    tmp = ncr(n-1, i-1)
    for f in fruit:
        total += tmp*f

print(total)