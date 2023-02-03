import io
import sys
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = [1]

for i in range(2, N+1):
    S = S + [i] + S

print(*S)