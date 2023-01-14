import io
import sys
_INPUT = """\
1
a
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input() for _ in range(N))

ma = 0
for i in range(N):
    tmp = S[i]
    cnt = 0
    for j in range(N):
        if S[j] == tmp: cnt += 1
    if cnt > ma:
        ma = cnt
        ans = tmp

print(ans)