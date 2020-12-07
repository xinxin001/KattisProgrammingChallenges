from sys import stdin
import math
# each iter square x4
#sqrt(square)
#
n = int(stdin.readline())
square = pow(4,n)
side = math.sqrt(square)
side +=1
points = pow(side,2)

print(int(points))