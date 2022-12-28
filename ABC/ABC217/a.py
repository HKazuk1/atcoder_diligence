import io
import sys
_INPUT = """\
a aa
"""
sys.stdin = io.StringIO(_INPUT)

S, T = input().split()

if S < T:
    print("Yes")
else:
    print("No")