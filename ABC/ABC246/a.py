import io
import sys
_INPUT = """\
-60 -40
-60 -80
-20 -80
"""
sys.stdin = io.StringIO(_INPUT)

xy = [list(map(int, input().split())) for _ in range(3)]

ans = [0]*2
if xy[0][0] == xy[1][0]:
    ans[0] = xy[2][0]
elif xy[1][0] == xy[2][0]:
    ans [0] = xy[0][0]
else:
    ans[0] = xy[1][0]

if xy[0][1] == xy[1][1]:
    ans[1] = xy[2][1]
elif xy[1][1] == xy[2][1]:
    ans [1] = xy[0][1]
else:
    ans[1] = xy[1][1]
print(*ans)