import io
import sys
_INPUT = """\
2 1
100 1
2
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
yum = []

mx = max(A)
for i in range(len(A)):
    if A[i] == mx:
        yum.append(i+1)

for i in B:
    if i in yum:
        print("Yes")
        exit()
print("No")