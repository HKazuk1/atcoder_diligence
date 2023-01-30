import io
import sys
_INPUT = """\
7
4 8 1 7 9 5 6
3 5 1 7 8 2 6
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = [0]*2

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                ans[0] += 1
            else:
                ans[1] += 1

print(ans[0],ans[1],sep="\n")