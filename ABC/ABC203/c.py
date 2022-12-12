# @u2dayo様のコードを参考にしました

import io
import sys
_INPUT = """\
3 2
5 5
2 1
2 2
"""
sys.stdin = io.StringIO(_INPUT)

n, k = map(int, input().split())
mat = []

for _ in range(n):
    a, b = map(int, input().split())
    mat.append((a, b))

# aを小さい順にソート
mat.sort()
now = k # 始めの所持金で村Kまで行ける
for i in range(n):
    a, b = mat[i]
    if now >= a:
        # 村A_iの人がB_i円 くれるので、即座に消費してB_i進む
        now += b
    else:
        break

print(now)
