from sys import stdin
import math 

def pts_diff(pt1, pt2):
    return [pt2[0]-pt1[0], pt2[1]-pt1[1]]

def pts_add(pt1, pt2):
    return [pt2[0]+pt1[0], pt2[1]+pt1[1]]

def center_pt(pt1, pt2):
    return [(pt2[0]+pt1[0])/2, (pt2[1]+pt1[1])/2]

def get_edge(edge, center):
    diff = pts_diff(edge, center)
    return pts_add(diff,center)

p1 = [int(x) for x in stdin.readline().split()]
p2 = [int(x) for x in stdin.readline().split()]
p3 = [int(x) for x in stdin.readline().split()]
p4 = []

p2p1 = pts_diff(p2,p1)
p3p1 = pts_diff(p3,p1)
p3p2 = pts_diff(p3,p2)

dist1 = math.sqrt(p2p1[0]**2 + p2p1[1]**2)
dist2 = math.sqrt(p3p1[0]**2 + p3p1[1]**2)
dist3 = math.sqrt(p3p2[0]**2 + p3p2[1]**2)

max = max(dist1,dist2,dist3)

if dist1 == max:
    center = center_pt(p1,p2)
    p4 = get_edge(p3, center)
if dist2 == max:
    center = center_pt(p1,p3)
    p4 = get_edge(p2, center)
if dist3 == max:
    center = center_pt(p2,p3)
    p4 = get_edge(p1, center)
print(str(int(p4[0])) + ' ' + str(int(p4[1])))
