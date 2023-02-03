import io
import sys
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
sl = []
tl = []

for i in range(N):
    s, t = map(str, input().split())
    sl.append(s)
    tl.append(t)
    
for i in range(N):
    nl = []
    for j in range(N):
        if i != j:
            nl.append(sl[j])
            nl.append(tl[j])
    
    if sl in nl and tl in nl:
        print("No")
        exit()

print("Yes")