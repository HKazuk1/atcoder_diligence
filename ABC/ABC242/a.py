import io
import sys
_INPUT = """\
50 500 100 1
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, X = map(int, input().split())

if A >= X:
    print(1)
elif A < X <= B:
    print(C/(B-A))
else:
    print(0)