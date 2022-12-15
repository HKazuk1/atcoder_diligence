import io
import sys
_INPUT = """\
1
1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
L = list(range(1, N+1))

A.sort()
if A == L: print("Yes")
else: print("No")