import io
import sys
_INPUT = """\
2 10
1 3
"""
sys.stdin = io.StringIO(_INPUT)

N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = set()

for i in range(N):
    if A[i] <= W:
        ans.add(A[i])

for i in range(N):
    for j in range(i+1, N):
        if A[i]+A[j] <= W:
            ans.add(A[i]+A[j])

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i]+A[j]+A[k] <= W:
                ans.add(A[i]+A[j]+A[k])

print(len(ans))