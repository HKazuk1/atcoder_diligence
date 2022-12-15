import io
import sys
_INPUT = """\
0 50
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
print(A * (B/100))