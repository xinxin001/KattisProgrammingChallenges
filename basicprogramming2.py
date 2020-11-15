from sys import stdin
from sys import exit
from collections import Counter

n, t = stdin.readline().split()
n = int(n)
t = int(t)

a = [int(d) for d in stdin.readline().split()]

if t == 1:
    sum = 7777
    values = set()
    for i in range(n):
        if sum-a[i] in values:
            print("Yes")
            exit(0)
        values.add(a[i])
    print("No")

if t == 2:
    print('Unique') if len(set(a))==n else print('Contains duplicate')

if t == 3:
    x,y = Counter(a).most_common(1)[0]
    print(x) if y > n/2 else print(-1)

if t == 4:
    a.sort()
    if n%2 == 1:
        print(a[len(a)//2])
    else:
        med1 = a[(len(a)//2)-1]
        med2 = a[(len(a)//2)]
        print(str(med1) + " " + str(med2))

if t == 5:
    values = []
    a.sort()
    for i in range(n):
        if a[i] > 99 and a[i] < 1000:
            values.append(str(a[i]))
    values = " ".join(values)
    print(values)


