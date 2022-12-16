import io
import sys
_INPUT = """\
99 99 98 
"""
sys.stdin = io.StringIO(_INPUT)

A = list(map(int, input().split()))
A.sort()
print(A[1] + A[2])