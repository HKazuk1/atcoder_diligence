import io
import sys
_INPUT = """\
3 3 2
"""
sys.stdin = io.StringIO(_INPUT)

N, K, A = map(int, input().split())
ans = (A + K - 1) % N
if ans == 0:
    ans = N
print(ans)