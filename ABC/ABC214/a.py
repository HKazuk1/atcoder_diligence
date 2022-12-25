import io
import sys
_INPUT = """\
126
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

if 1 <= N <= 125:
    print(4)
elif 126 <= N <= 211:
    print(6)
else:
    print(8)