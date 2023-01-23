import io
import sys
_INPUT = """\
1
1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
L = [False] * 360
L[0] = True

p = 0
for i in A:
    p += i
    p %= 360
    L[p] = True

ans = 0
tmp = 0
for i in range(361):
    if L[i%360]:
        ans = max(ans, tmp)
        tmp = 0
    tmp += 1

print(ans)