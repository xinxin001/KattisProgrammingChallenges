from sys import stdin

n = int(stdin.readline())
t = [int(x) for x in stdin.readline().split()]

t.sort(reverse=True)

#everyday choose which tree is taking more time to grow
#end of planting trees, add it to elapsed days+1
maxd = 0
day = 0
for i in t:
    day += 1
    maxd -= 1
    maxd = max(i, maxd)
    
print(day+maxd+1)