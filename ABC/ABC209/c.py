import io
import sys
_INPUT = """\
2
1 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
C = list(map(int, input().split()))
C.sort()

ans = 1
for i in range(N):
    ans = ans * max(0, C[i] - i) % 1000000007
print(ans)