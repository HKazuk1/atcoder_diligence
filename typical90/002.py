import io
import sys
_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)


from itertools import product

# カッコ列 s が整合しているか判定
def isvalid(s):
    score = 0
    for c in s:
        if c == '(':
            score += 1
        else:
            score -= 1

        # 途中で 0 を下回るとダメ
        if score < 0:
            return False

    # 最後に 0 なら True、そうでなければ False
    return (score == 0)

N = int(input())
for s in product(['(', ')'], repeat=N):
    if isvalid(s):
        # リストを文字列に
        print(*s, sep='')