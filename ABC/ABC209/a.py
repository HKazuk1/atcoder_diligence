import io
import sys
_INPUT = """\
10 100
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

if A <= B:
    print(B-A+1)
else:
    print(0)