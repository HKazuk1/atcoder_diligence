import io
import sys
_INPUT = """\
4 100
6 2
1 5
3 9
8 7
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(reverse=True)

ans = 0
for i in range(N):
    ans += AB[i][0] * min(W, AB[i][1])
    W -= min(W, AB[i][1])
print(ans)