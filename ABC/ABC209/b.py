import io
import sys
_INPUT = """\
8 30
3 1 4 1 5 9 2 6
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    # もしA[i]が偶数番目だったら
    if i%2 == 1:
        X -= (A[i]-1)
    else:
        X -= A[i]

if X >= 0:
    print("Yes")
else:
    print("No")