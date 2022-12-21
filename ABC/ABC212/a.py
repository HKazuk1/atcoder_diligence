import io
import sys
_INPUT = """\
100 2
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

if 0 < A and B == 0:
    print("Gold")
elif A == 0 and 0 < B:
    print("Silver")
else:
    print("Alloy")