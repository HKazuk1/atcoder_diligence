import io
import sys
_INPUT = """\
12
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

for i in range(1, N+1):
    ans = (1+i)*i // 2
    if ans >= N:
        print(i)
        break