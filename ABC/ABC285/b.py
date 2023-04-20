import io
import sys
_INPUT = """\
6
abcbac
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()

for i in range(1, N):
    for j in range(1, N+1):
        if i+j > N:
            print(j-1)
            break
        if S[j-1] == S[j+i-1]:
            print(j-1)
            break
    