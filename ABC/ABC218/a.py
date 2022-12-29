import io
import sys
_INPUT ="""\
4
oooxoox
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

if S[N-1] == "o":
    print("Yes")
else:
    print("No")