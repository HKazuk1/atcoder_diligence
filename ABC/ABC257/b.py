import io
import sys
_INPUT = """\
10 6 9
1 3 5 7 8 9
1 2 3 4 5 6 5 6 2
"""
sys.stdin = io.StringIO(_INPUT)

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in L:
    if A[i-1] != N:
        if A[i-1]+1 not in A:
            A[i-1] += 1
print(*A)