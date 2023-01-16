import io
import sys
_INPUT ="""\
270 750

"""
sys.stdin = io.StringIO(_INPUT)

X, Y = map(int, input().split())

cnt = 0
while True:
    if X >= Y:
        print(cnt)
        exit()
    X += 10
    cnt += 1