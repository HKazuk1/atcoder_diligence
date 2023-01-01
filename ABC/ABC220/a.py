import io
import sys
_INPUT = """\
630 940 314
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C = map(int, input().split())

for i in range(A, B+1):
    if i%C == 0:
        print(i)
        exit()
print(-1)