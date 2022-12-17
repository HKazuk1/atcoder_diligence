import io
import sys
_INPUT = """\
7 1000000000000
99 8 2 4 43 5 3
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
a = list(map(int, input().split()))

order = [(a[i] << 32) + i for i in range(N)]
# order = [a[i] for i in range(N)]
# print(order)
order.sort()
# for i in order:
#     print(bin(i))

# print(bin((1<<32)-1))
answer = [K // N for i in range(N)]
for i in range(K % N):
    # print(order[i] & ((1 << 32) - 1))
    answer[order[i] & ((1 << 32) - 1)] += 1
for x in answer:
    print(x)