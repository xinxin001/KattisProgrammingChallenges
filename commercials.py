from sys import stdin

n, p = stdin.readline().split()
n = int(n)
p = int(p)

arr = [(int(x)-p) for x in stdin.readline().split()]

bestsum = 0
currentsum = 0

#Maximum subarray problem from wikipedia. 

for c in arr:
    currentsum = max(0, currentsum + c)
    bestsum = max(bestsum, currentsum)

print(bestsum)
