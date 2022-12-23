import io
import sys
_INPUT = """\
5
3 1 4 15 9
"""
sys.stdin = io.StringIO(_INPUT)


import copy

N = int(input())
A = list(map(int, input().split()))
sort_A = sorted(copy.copy(A))

for i in range(N):
    if sort_A[N-2] == A[i]:
        print(i+1)
        exit()