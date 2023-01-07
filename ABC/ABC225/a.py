import io
import sys
_INPUT ="""\
aba
"""
sys.stdin = io.StringIO(_INPUT)

S = set(input())

if len(S) == 3:
    print('6')
elif len(S) == 2:
    print('3')
else:
    print('1')