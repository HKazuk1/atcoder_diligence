import io
import sys
_INPUT = """\
5 2 3 2
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, D = map(int, input().split())

ans = -1
diff = C*D-B
if 0 < diff:
    ans = (A+diff-1)//diff

print(ans)