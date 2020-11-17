from sys import stdin

string = stdin.readline().replace('\n', '')

def isPeriodic(k):
    if(len(string)%k != 0): return False
    arr = [string[s:s+k] for s in range(0,len(string), k)]
    for j in range(1, len(arr)):
        prev = arr[j-1]
        prev = prev[-1] + prev[:-1]

        if prev != arr[j]: return False
    return True

for i in range(1,len(string)+1):
    if isPeriodic(i):
        print(i)
        break
# abbaab abaabba