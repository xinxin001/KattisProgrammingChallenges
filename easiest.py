from sys import stdin

def sumOfDigits(integer):
    intlist = [int(d) for d in str(integer)]
    return sum(intlist)

n = []

while(True):
    inp = int(stdin.readline())
    if(inp == 0):
        break
    n.append(inp)

for num in n:
    p = 11
    while(sumOfDigits(p*num) != sumOfDigits(num)):
        p += 1
    print(p)