import io
import sys
_INPUT = """\
1
a
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
print(input()[-1])