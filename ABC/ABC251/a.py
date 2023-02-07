import io
import sys
_INPUT = """\
a
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
if len(S) == 1:
    print(S*6)
elif len(S) == 2:
    print(S*3)
else:
    print(S*2)