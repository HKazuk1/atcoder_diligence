import io
import sys
_INPUT = """\
31 415926 5

"""
sys.stdin = io.StringIO(_INPUT)

A, B, K = map(int, input().split())
cnt = 0
while A < B:
    A *= K
    cnt += 1
print(cnt)