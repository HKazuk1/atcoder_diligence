import io
import sys
_INPUT ="""\
1
1 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
L = set(tuple(list(map(int, input().split()))) for _ in range(N))
print(len(L))