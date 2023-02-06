import io
import sys
_INPUT = """\
4 3 3
"""
sys.stdin = io.StringIO(_INPUT)

N, A, B = map(int, input().split())

for i in range(N*A):
    S = ''
    for j in range(N*B):
        if ((i//A)+(j//B))%2 != 0:
            S += '#'
        else:
            S += '.'
    print(S)