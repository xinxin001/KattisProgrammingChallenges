from sys import stdin

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    v1 = [int(x) for x in stdin.readline().split()]
    v2 = [int(x) for x in stdin.readline().split()]
    #have 1 vector sorted asc, other sorted desc
    #smallest dot product is when avoiding large number multiplcation
    v1.sort()
    v2.sort(reverse=True)
    sum = 0
    for j in range(n):
        sum += v1[j]*v2[j]
    print("Case #" + str(i+1) +": " + str(sum))