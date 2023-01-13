import io
import sys
_INPUT = """\
42
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
print(f"AGC{N+1:03}" if N > 41 else f"AGC{N:03}")