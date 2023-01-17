import io
import sys
_INPUT = """\
5
315 271
-2 -621
-205 -511
-952 482
165 463
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        dist_x = xy[i][0] - xy[j][0]
        dist_y = xy[i][1] - xy[j][1]
        dist = (dist_x**2 + dist_y**2) ** 0.5
        ans = max(ans, dist)

print(ans)