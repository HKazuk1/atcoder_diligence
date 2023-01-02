import io
import sys
_INPUT ="""\
5 5
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
print(32**(A-B))