import io
import sys
_INPUT = """\
2 1
"""
sys.stdin = io.StringIO(_INPUT)

x, y = map(int, input().split())

if x == y:
    print(x)
else:
    print(3-(x+y))