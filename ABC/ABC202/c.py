import io
import sys
_INPUT = """\
3
2 3 3
1 3 3
1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = defaultdict(int)

for i in range(n):
    d[b[c[i]-1]] += 1
    
ans = 0
for x in a:
    ans += d[x]

print(ans)