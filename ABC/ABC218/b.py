import io
import sys
_INPUT ="""\
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""
sys.stdin = io.StringIO(_INPUT)

P = list(map(int, input().split()))

for i in P:
    print(chr(96+i), end="")