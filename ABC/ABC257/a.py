import io
import sys
_INPUT = """\
5 12
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
print(chr(65+(X-1)//N))