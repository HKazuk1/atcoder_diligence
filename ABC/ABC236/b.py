import io
import sys
_INPUT = """\
4
3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
"""
sys.stdin = io.StringIO(_INPUT)


from collections import Counter

N = int(input())
A = sorted(list(map(int, input().split())))

c = Counter(A)
print(c.most_common()[-1][0])