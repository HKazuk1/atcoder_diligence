import io
import sys
_INPUT = """\
20
SRSRSSRSSSRSRRRRRSRR
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
T = input()
d = 0
xy = [0]*2

for i in T:
    if i == 'S':
        if d == 0:
            xy[0] += 1
        elif d == 1:
            xy[1] -= 1
        elif d == 2:
            xy[0] -= 1
        else:
            xy[1] += 1
    else:
        d = (d+1)%4

print(*xy)