from sys import stdin

inp = stdin.readline().split()
h = int(inp[0])
path = []
if len(inp) > 1:
    path = list(inp[1])

nodes = (2**(h+1))-1

pos = 1
for dir in path:
    pos *= 2
    if(dir == "R"):
        pos += 1
        
pos = nodes - pos + 1

print(pos)