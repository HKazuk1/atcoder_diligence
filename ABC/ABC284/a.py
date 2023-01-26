import io
import sys
_INPUT = """\
4
2023
Year
New
Happy
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = [input() for _ in range(N)][::-1]
for i in range(N):
    print(S[i])