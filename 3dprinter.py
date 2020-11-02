from sys import stdin

n = int(stdin.readline())

printers = 1
days = 1

while printers < n:
    printers *= 2
    days+=1
    

print(days)