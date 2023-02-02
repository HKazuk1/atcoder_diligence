import io
import sys
_INPUT  = """\
246 402
"""
sys.stdin = io.StringIO(_INPUT)

import math

A, B = map(int, input().split())
d = math.sqrt(A**2 + B**2)
print(A/d, B/d)