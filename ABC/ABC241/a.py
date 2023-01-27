import io
import sys
_INPUT = """\
0 0 0 0 0 0 0 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)

a = list(map(int, input().split()))

ans = a[0]
for i in range(2):
    ans = a[ans]
print(ans)