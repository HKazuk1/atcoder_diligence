import io
import sys
_INPUT = """\
5 5
ooooo
oooxx
xxooo
oxoxo
xxxxx
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                # print(i,j)
                break
            if k == M-1:
                ans += 1
        
print(ans)