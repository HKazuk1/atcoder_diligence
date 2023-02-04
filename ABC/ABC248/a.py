import io
import sys
_INPUT = """\
012345678
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
flg = [1 for _ in range(10)]
for i in range(9):
    flg[int(S[i])] = 0
for i in range(10):
    if flg[i]:
        print(i)