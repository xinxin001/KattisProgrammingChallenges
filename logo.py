from sys import stdin
import math

n = int(stdin.readline())

for i in range(n):
    c = int(stdin.readline())

    commands = []
    pos = [0,0]

    angle = 0
    for i in range(c):
        line = stdin.readline().split()
        line[1] = int(line[1])
        commands.append(line)

    for command in commands:
        if command[0] == 'fd':
            pos[0] += command[1] * math.sin(angle*(math.pi/180))
            pos[1] += command[1] * math.cos(angle*(math.pi/180))
        if command[0] == 'bk':
            pos[0] -= command[1] * math.sin(angle*(math.pi/180))
            pos[1] -= command[1] * math.cos(angle*(math.pi/180))
        if command[0] == 'lt':
            angle += command[1]
        if command[0] == 'rt':
            angle -= command[1]

    distance = round(math.sqrt((pos[0]**2) + (pos[1]**2)))

    print(distance)