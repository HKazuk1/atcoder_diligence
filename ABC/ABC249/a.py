import io
import sys
_INPUT = """\
1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, D, E, F, X = map(int, input().split())

t = X//(A+C)
a = X//(D+F)

if A > X%(A+C):
    tt = B*(X%(A+C) + (A*t))
else:
    tt = B*(A + (A*t))

if D > X%(D+F):
    aa = E*(X%(D+F) + (D*a))
else:
    aa = E*(D + (D*a))

if tt == aa:
    print("Draw")
elif tt > aa:
    print("Takahashi")
else:
    print("Aoki")