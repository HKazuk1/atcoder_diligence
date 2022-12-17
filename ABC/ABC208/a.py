import io
import sys
_INPUT = """\
100 600
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
if A*6 >= B and A <= B:
    print("Yes")
else:
    print("No")