import io
import sys
_INPUT = """\
2 5 2
"""
sys.stdin = io.StringIO(_INPUT)

a = list(map(int, input().split()))
a.sort()

if a[0] == a[1]:
    print(a[2])
elif a[1] == a[2]:
    print(a[0])
else:
    print(0)