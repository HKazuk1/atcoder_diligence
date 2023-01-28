import io
import sys
_INPUT = """\
4 4
000000
123456
987111
000000
000
111
999
111
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = [input()[-3:] for _ in range(N)]
T = [input() for _ in range(M)]

ans = 0
for i in S:
    for j in T:
        if i == j:
            ans += 1
            break
print(ans)