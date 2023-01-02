import io
import sys
_INPUT ="""\
abcde
abcde
"""
sys.stdin = io.StringIO(_INPUT)

S = list(input())
T = list(input())

if S == T:
    print("Yes")
    exit()

for i in range(len(S)-1):
    s = list(S)
    s[i], s[i+1] = s[i+1], s[i]
    if s == T:
        print("Yes")
        exit()
print("No")