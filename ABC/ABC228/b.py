import io
import sys
_INPUT ="""\
20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0]*N

while True:
    if cnt[X-1] == 1:
        print(sum(cnt))
        exit()
    cnt[X-1] = 1
    X = A[X-1]