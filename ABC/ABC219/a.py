import io
import sys
_INPUT = """\
90
"""
sys.stdin = io.StringIO(_INPUT)

X = int(input())

if 0 <= X < 40:
    print(40-X)
elif 40 <= X < 70:
    print(70-X)
elif 70 <= X < 90:
    print(90-X)
else:
    print("expert")