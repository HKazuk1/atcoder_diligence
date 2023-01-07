import io
import sys
_INPUT ="""\
4
2 4
1 4
2 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N-1)]
l = [0]*N

for i in ab:
    l[i[0]-1] += 1
    l[i[1]-1] += 1

for i in l:
    if i == N-1:
        print("Yes")
        exit()
print("No")