import io
import sys
_INPUT = """\
abra
cad
abra
123
"""
sys.stdin = io.StringIO(_INPUT)

S = [input() for _ in range(3)]
T = input()

for i in range(len(T)):
    print(S[int(T[i]) - 1], end="")