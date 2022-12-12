import io
import sys
_INPUT = """\
5 6 4
"""
sys.stdin = io.StringIO(_INPUT)

a = list(map(int, input().split()))
print(21 - sum(a))