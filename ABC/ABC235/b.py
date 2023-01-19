import io
import sys
_INPUT = """\
4
27 1828 1828 9242
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
H = list(map(int, input().split()))

ans = H[0]
for i in range(len(H)-1):
    if H[i] < H[i+1]:
        ans = H[i+1]
    else:
        print(ans)
        exit()
print(H[-1])