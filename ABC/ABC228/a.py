import io
import sys
_INPUT ="""\
7 20 12
"""
sys.stdin = io.StringIO(_INPUT)

S, T, X = map(int, input().split())
if S < T:
    if S <= X < T:
        print("Yes")
    else:
        print("No")
else:
    if X < T or S <= X:
        print("Yes")
    else:
        print("No")