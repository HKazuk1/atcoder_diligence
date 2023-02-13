import io
import sys
_INPUT = """\
5 4
-o--
----
----
----
-o--

"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
idx = []

for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            idx.append([i, j])

ans = abs(idx[0][0]-idx[1][0]) + abs(idx[0][1]-idx[1][1])
print(ans)