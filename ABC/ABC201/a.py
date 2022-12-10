import io
import sys
_INPUT = """\
5 1 3
"""
sys.stdin = io.StringIO(_INPUT)


a = list(map(int, input().split()))
a.sort()

if a[2]-a[1] == a[1]-a[0]:
    print("Yes")
else:
    print("No")