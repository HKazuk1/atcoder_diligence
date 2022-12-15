import io
import sys
_INPUT ="""\
20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
"""
sys.stdin = io.StringIO(_INPUT)

# 全探索はTLE
# N = int(input())
# A = list(map(int, input().split()))

# ans = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if A[i] != A[j]:
#             ans += 1
# print(ans)


from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
# Cの値を取り出す
CV = C.values()
# CVをlist型に
CV = list(CV)

ans = N * (N-1) // 2
for i in range(len(CV)):
    ans -= CV[i] * (CV[i]-1) // 2

print(ans)