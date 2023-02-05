import io
import sys
_INPUT = """\
atcoder
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
s = set(S)

if len(S) != len(s) or S.islower() or S.isupper():
    print("No")
else:
    print("Yes")