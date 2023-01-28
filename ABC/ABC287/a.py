import io
import sys
_INPUT = """\
1
For
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = [input() for _ in range(N)]

agree = 0
for i in S:
    if i == "For":
        agree += 1

if agree > N//2:
    print("Yes")
else:
    print("No")