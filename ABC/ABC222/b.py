import io
import sys
_INPUT = """\
3 90
89 89 90
"""
sys.stdin = io.StringIO(_INPUT)

N, P = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in a:
    if i < P:
        ans += 1
print(ans)