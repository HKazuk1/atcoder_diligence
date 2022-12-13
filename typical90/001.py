import io
import sys
_INPUT = """\
3 34
1
8 13 26
"""
sys.stdin = io.StringIO(_INPUT)

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)
ok = -1
ng = L

while abs(ok - ng) > 1:
    mid = (ok+ng)//2
    slice = 0
    pre = 0
    for i in A:
        # print(f"ok:{ok} ng:{ng} mid:{mid} slice:{slice} pre:{pre} i:{i}")
        if i-pre >= mid:
            slice += 1
            pre = i
    if slice > K:
        ok = mid
    else:
        ng = mid
print(ok)