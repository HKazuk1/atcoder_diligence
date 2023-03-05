import io
import sys
_INPUT = """\
3 9
3 1
3 2
1 2
2 1
3 1
3 2
1 2
3 2
3 3

"""
sys.stdin = io.StringIO(_INPUT)

N, Q = map(int, input().split())
ev = [list(map(int, input().split())) for _ in range(Q)]
red = [0]*N
yellow = [0]*N

for query in ev:
    if query[0] == 1:
        yellow[query[1]-1] += 1
    elif query[0] == 2:
        red[query[1]-1] += 1
    else:
        if red[query[1]-1] == 1 or yellow[query[1]-1] == 2:
            print("Yes")
        else:
            print("No")