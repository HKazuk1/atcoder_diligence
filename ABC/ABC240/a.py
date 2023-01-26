import io
import sys
_INPUT = """\
3 5
"""
sys.stdin = io.StringIO(_INPUT)

a, b = (map(int, input().split()))

if abs(a-b) == 9 or abs(a-b) == 1:
    print("Yes")
else:
    print("No")