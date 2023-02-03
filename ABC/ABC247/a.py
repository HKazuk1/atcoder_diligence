import io
import sys
_INPUT = """\
1111
"""
sys.stdin = io.StringIO(_INPUT)

print('0' + input()[:3])