import io
import sys
_INPUT ="""\
3 3
2 1 4
3 1 3
6 4 1
"""
sys.stdin = io.StringIO(_INPUT)

H, W =map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(W-1):
    for ii in range(i+1, W):
        for j in range(H-1):
            for jj in range(j+1, H):
                if A[i][j] + A[ii][jj] > A[ii][j] + A[i][jj]:
                    print("No")
                    exit()
print("Yes")