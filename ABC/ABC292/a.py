import io
import sys
_INPUT = """\
abc
"""
sys.stdin = io.StringIO(_INPUT)

print(input().upper())