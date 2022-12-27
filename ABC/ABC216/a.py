import io
import sys
_INPUT = """\
15.8
"""
sys.stdin = io.StringIO(_INPUT)

X, Y = map(int, input().split('.'))

if 0 <= Y <= 2:
    print(f"{X}-")
elif 3 <= Y <= 6:
    print(X)
else:
    print(f"{X}+")