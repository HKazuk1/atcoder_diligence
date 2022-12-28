import io
import sys
_INPUT = """\
AGC
ABC
ARC
"""
sys.stdin = io.StringIO(_INPUT)

S = [input() for _ in range(3)]
S.sort()

if S[0] != "ABC":
    print("ABC")
elif S[1] != "AGC":
    print("AGC")
elif S[2] != "AHC":
    print("AHC")
else:
    print("ARC")