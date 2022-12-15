import io
import sys
_INPUT = """\
191
"""
sys.stdin = io.StringIO(_INPUT)


import math

N = int(input())
N *= 1.08
N = math.floor(N)

if N == 206:
    print("so-so")
elif N < 206:
    print("Yay!")
else:
    print(":(")

#- リスト内包表記を用いた実装例
N = round(int(input()) * 1.08)
print("Yay!" if N < 206 else "so-so" if N == 206 else ":(")