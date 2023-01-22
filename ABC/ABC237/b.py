import io
import sys
_INPUT = """\
4 3
1 2 3
4 5 6
7 8 9
10 11 12
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

B = [[A[j][i] for j in range(H)] for i in range(W)]
for b in B:
  print(*b)