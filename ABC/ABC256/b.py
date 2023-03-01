import io
import sys
_INPUT = """\
10
2 2 4 1 1 1 4 2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
l = []
ans = 0

for i in A:
    l.append(1)
    for j in range(len(l)):
        l[j] += i

for i in l:
    if i > 4:
        ans += 1

print(ans)