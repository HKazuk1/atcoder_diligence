import io
import sys
_INPUT ="""\
2.5
"""
sys.stdin = io.StringIO(_INPUT)


X = float(input())
if X-int(X) >= .5:
    print(int(X)+1)
else:
    print(int(X))