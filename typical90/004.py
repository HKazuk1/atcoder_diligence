import io
import sys
_INPUT = """\
10 10
83 86 77 65 93 85 86 92 99 71
62 77 90 59 63 76 90 76 72 86
61 68 67 79 82 80 62 73 67 85
79 52 72 58 69 67 93 56 61 92
79 73 71 69 84 87 98 74 65 70
63 76 91 80 56 73 62 70 96 81
55 75 84 77 86 55 96 79 63 57
74 95 82 95 64 67 84 64 93 50
87 58 76 78 88 84 53 51 54 99
82 60 76 68 89 62 76 86 94 89
"""
sys.stdin = io.StringIO(_INPUT)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 各行の合計を格納する配列 Wttl(W_total) を宣言
Wttl = []
# 各列の合計を格納する配列 Httl を宣言
Httl = []

for i in range(H):
    tmp = 0
    for j in range(W):
        tmp += A[i][j]
    Wttl.append(tmp)

for i in range(W):
    tmp = 0
    for j in range(H):
        tmp += A[j][i]
    Httl.append(tmp)

# print(Wttl, "\n", Httl)

for i in range(H):
    for j in range(W):
        ans = Wttl[i] + Httl[j] - A[i][j]
        print(ans, end=" ")
    print("")