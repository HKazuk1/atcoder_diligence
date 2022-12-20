import io
import sys
_INPUT = """\
123 123
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int,input().split())
print((A-B)/3 + B)