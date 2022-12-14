import io
import sys
_INPUT = """\
4
8 9 10 11
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in A:
    if i > 10:
        ans += (i - 10)

print(ans)