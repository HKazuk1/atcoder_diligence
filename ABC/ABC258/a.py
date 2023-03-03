import io
import sys
_INPUT = """\
60
"""
sys.stdin = io.StringIO(_INPUT)

K = int(input())
if K < 60:
    print(f"21:{K:02}")
else:
    print(f"22:{K-60:02}")