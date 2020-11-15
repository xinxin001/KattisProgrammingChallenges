from sys import stdin
from collections import Counter

string = [char for char in stdin.readline()]
string.remove('\n')
charcount = Counter(string)

oddcount = 0
removechars = 0
for key in charcount:
    if charcount[key]%2 == 1:
        oddcount += 1
        if oddcount > 1:
            removechars += 1

print(removechars)