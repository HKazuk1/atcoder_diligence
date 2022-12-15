import io
import sys
_INPUT = """\
-3 -3 5
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C = map(int, input().split())

if C%2 == 0:
    # 正負関係なくpow(A,C)とpow(B,C)の値が等しくなる
    if A+B == 0 or A-B == 0:
        print('=')
    elif abs(A) > abs(B):
        print('>')
    else:
        print('<')
else:
    # A、Bの符号が一致するときのみ値が等しくなる
    if A-B == 0:
        print('=')
    elif A > B:
        print('>')
    else:
        print('<')