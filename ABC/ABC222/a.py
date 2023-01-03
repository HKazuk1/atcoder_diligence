import io
import sys
_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

print(input().zfill(4))