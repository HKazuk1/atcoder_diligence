import io
import sys
_INPUT ="""\
.#
#.
"""
sys.stdin = io.StringIO(_INPUT)

S = [input() for _ in range(2)]
if (S[0] == ".#" and S[1] == "#.") or (S[0] == "#." and S[1] == ".#"):
    print("No")
else:
    print("Yes")