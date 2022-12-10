import io
import sys
_INPUT = """\
ooo???xxxx
"""
sys.stdin = io.StringIO(_INPUT)

s = input()

ans = 0

for x in range(10000):
    ok = True
    
    # xを文字列にし4桁になるようにゼロ埋め
    x = str(x)
    x = x.zfill(4)
    
    for i in range(10):
        if s[i] == "o":
            if str(i) not in x:
                ok = False
        if s[i] == "x":
            if str(i) in x:
                ok = False
    
    if ok == True:
        ans += 1

print(ans)
    