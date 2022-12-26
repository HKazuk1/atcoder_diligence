import io
import sys
_INPUT = """\
1000000000000000000
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

for i in range(100):
    if 2 ** i == N:
        print(i)
        exit()
    elif 2 ** i >= N:
        print(i-1)
        exit()