import io
import sys
_INPUT = """\
4
12 34 56 78
1000
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumN = 0
for i in range(N):
    sumN += A[i]

n = X // sumN
sumN *= n
ans = n*N

for i in range(N):
    sumN += A[i]
    if sumN > X:
        print(ans+i+1)
        exit()