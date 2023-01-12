import io
import sys
_INPUT ="""\
229 390
"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

while A > 0 and B > 0:
    if A%10 + B%10 >= 10:
        print("Hard")
        exit()
    A //= 10
    B //= 10
print("Easy")