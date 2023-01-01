import io
import sys
_INPUT = """\
7
123 456
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
A, B = input().split()

ans = 0
def f(K, N):
    ans = 0
    for i in range(1, len(N)+1):
        ans += int(N[-i]) * K**(i-1)
    return ans

print(f(K, A) * f(K, B))