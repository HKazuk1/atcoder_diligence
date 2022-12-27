import io
import sys
_INPUT = """\
4
sypdgidop bkseq
bajsqz hh
ozjekw mcybmtt
qfeysvw dbo
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ST = set(input() for _ in range(N))

if N == len(ST):
    print("No")
else:
    print("Yes")