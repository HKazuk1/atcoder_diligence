import io
import sys
_INPUT = """\
3
Everest 8849
K2 8611
Kangchenjunga 8586
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
st = []
for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    st.append([t,s])

st.sort(reverse=True)

print(st[1][1])