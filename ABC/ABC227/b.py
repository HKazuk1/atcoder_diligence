import io
import sys
_INPUT = """\
5
666 777 888 777 666
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(map(int, input().split()))
cnt = [0]*N

for i in range(len(S)):
    for a in range(1, 200):
        if cnt[i] == 1:
            break
        for b in range(1, 200):
            if cnt[i] == 1:
                break
            if 4*a*b + 3*a + 3*b == S[i]:
                cnt[i] += 1
                break
            
print(N - sum(cnt))