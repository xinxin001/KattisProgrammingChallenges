from sys import stdin

def win_if_start(min, max):
    if (max % min == 0): return True
    switch = win_if_start(max % min, min)
    if max >= min * 2:
        return True 
    else:
     return not switch


n, m = [int(x) for x in stdin.readline().split()]
min = min(n,m)
max = max(n,m)

if win_if_start(min, max):
    print('win')
else:
    print('lose')