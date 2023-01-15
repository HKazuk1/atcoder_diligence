import io
import sys
_INPUT = """\
abc
ijk
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()
K = ord(S[0]) - ord(T[0])
for i in range(len(S)):
    if (ord(S[i]) - ord(T[i]))%26 != K%26:
        print("No")
        exit()
print("Yes")