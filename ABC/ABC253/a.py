import io
import sys
_INPUT = """\
2 5 3
"""
sys.stdin = io.StringIO(_INPUT)

a, b, c = map(int, input().split())
if a <= b <= c or c <= b <= a:
    print("Yes")
else:
    print("No")