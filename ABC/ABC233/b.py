import io
import sys
_INPUT = """\
4 13
merrychristmas
"""
sys.stdin = io.StringIO(_INPUT)

L, R = map(int, input().split())
S = input()
print(S[:L-1] + S[L-1:R][::-1] + S[R:])