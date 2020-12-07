from sys import stdin

w, p = stdin.readline().split() 
w =  int(w)
p = int(p)

locations = [int(x) for x in stdin.readline().split()]
spaces = [None]*(w+1)
spaces[w] = True
for loc in locations:
    spaces[loc] = True
    spaces[w-loc] = True

for i in range(p):
    for j in range(i+1, p):
        spaces[locations[j] - locations[i]] = True

for i in range(w+1):
    if(spaces[i] == True):
        print(i, end=' ')
