from sys import stdin

n = int(stdin.readline())
a = []
dicti = {'W':n}

for i in range(n):
    a.append(stdin.readline().replace('\n', ""))
for i in range(n):
    count = 0
    d = dicti
    for char in a[i]:
        if char not in d:
            d[char] = {'W':1}
        d = d[char]
        d['W'] += 1
        count = d['W']
    
    print(count-2)