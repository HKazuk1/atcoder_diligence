import io
import sys
_INPUT = """\
aba
"""
sys.stdin = io.StringIO(_INPUT)

print("".join(sorted(input())))