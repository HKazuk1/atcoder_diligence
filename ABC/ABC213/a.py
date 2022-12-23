import io
import sys
_INPUT = """\
10 12
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

for i in range(256):
    if A ^ i == B:
        print(i)
        exit()