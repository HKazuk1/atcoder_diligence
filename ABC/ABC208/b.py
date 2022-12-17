import io
import sys
_INPUT = """\
10000000
"""
sys.stdin = io.StringIO(_INPUT)


from math import factorial

P = int(input())

cnt = 0
while P > 0:
    for i in range(10, 0, -1):
        if P >= factorial(i):
            P -= factorial(i)
            cnt += 1
            
            # 同じ硬貨が複数支払いに使われる可能性があるので
            # 一度for文を抜ける
            break

print(cnt)