import io
import sys
_INPUT = """\
11
3 1 4 1 5 9 2 6 5 3 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
a = set(list(map(int, input().split())))
print(len(a))