import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())

for i in range(K):
    print(chr(65+i), sep='', end="")