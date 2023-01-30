import io
import sys
_INPUT = """\
100000 1 1 1

"""
sys.stdin = io.StringIO(_INPUT)

V, A, B, C = map(int, input().split())
v = V % (A+B+C)
if v < A:
    print('F')
elif v < (A+B):
    print('M')
else:
    print('T')