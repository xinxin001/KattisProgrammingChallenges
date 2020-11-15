from sys import stdin

n, t = stdin.readline().split()
n = int(n)
t = int(t)

tasks = [int(d) for d in stdin.readline().split()]

count = 0
for i in range(n):
    if t-tasks[i] >= 0:
        t -= tasks[i]
        count += 1
    else:
        break

print(count)
