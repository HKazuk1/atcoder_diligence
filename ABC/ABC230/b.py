import io
import sys
_INPUT = """\
ox
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = "oxx"*10**5
print("Yes" if S in T else "No")