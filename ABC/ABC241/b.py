import io
import sys
_INPUT = """\
5 2
1 2 3 4 5
5 5
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in B:
    if i in A:
        A.remove(i)
    else:
        print("No")
        exit()
print("Yes")