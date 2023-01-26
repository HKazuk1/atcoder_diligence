import io
import sys
_INPUT = """\
4
3
1 2 3
2
20 23
10
6 10 4 1 5 9 8 6 5 1
1
1000000000
"""
sys.stdin = io.StringIO(_INPUT)

T = int(input())
test = []
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test.append(A)

ans = []
for i in range(T):
    tmp = 0
    for j in range(len(test[i])):
        if test[i][j]%2 == 1:
            tmp += 1
    print(tmp)