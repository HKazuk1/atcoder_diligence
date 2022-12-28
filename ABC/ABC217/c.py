import io
import sys
_INPUT = """\
3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
p = list(map(int, input().split()))
q = [0]*N

for i in range(N):
    q[p[i]-1] = i+1

print(*q)