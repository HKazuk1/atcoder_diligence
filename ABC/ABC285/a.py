import io
import sys
_INPUT = """\
2 8
"""
sys.stdin = io.StringIO(_INPUT)

a, b = map(int, input().split())

if a*2 == b or a*2+1 == b:
    print("Yes")
else:
    print("No")
    