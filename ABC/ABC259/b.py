import io
import sys
_INPUT = """\
2 2 180
"""
sys.stdin = io.StringIO(_INPUT)

from math import sin, cos, radians

a, b, d = map(int, input().split())
d = radians(d)
print(a*cos(d)-b*sin(d), a*sin(d)+b*cos(d))