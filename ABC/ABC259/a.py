import io
import sys
_INPUT = """\
38 20 17 168 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M, X, T, D = map(int, input().split())

if M >= X:
    print(T)
else:
    print(T-((X-M)*D))