import io
import sys
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

X = int(input())
if X >= 100 and X%100 == 0:
    print("Yes")
else:
    print("No")