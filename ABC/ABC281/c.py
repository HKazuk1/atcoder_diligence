import io
import sys
_INPUT = """\
3 600
180 240 120
"""
sys.stdin = io.StringIO(_INPUT)


from itertools import accumulate

n, t = map(int, input().split())
a = list(map(int, input().split()))

# 累積和を計算しaaに格納
aa = list(accumulate(a))

# 入力例1の一周540secはt=600のとき1周+60secなので、
# t%sum(a)でプレイリスト一周分でtの位置がわかるようにする
t = t%aa[-1]

# プレイリストの累積和とtを順に比較していく
for i in range(n):
    # tがi曲目の途中か判定
    if t < aa[i]:
        # tの位置は、曲iの時間 - (曲iの累積和 - t)で求まる
        ans = a[i] - (aa[i]-t)
        print(i+1, ans)
        exit()