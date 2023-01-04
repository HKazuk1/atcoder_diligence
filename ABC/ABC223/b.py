import io
import sys
_INPUT ="""\
abracadabra
"""
sys.stdin = io.StringIO(_INPUT)

S = input()

mn = S
mx = S
for i in range(len(S)):
    shift_s = S[i:] + S[:i]
    mn = min(mn, shift_s)
    mx = max(mx, shift_s)

print(mn + "\n" + mx)