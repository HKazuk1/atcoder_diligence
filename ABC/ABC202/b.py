import io
import sys
_INPUT = """\
0601889
"""
sys.stdin = io.StringIO(_INPUT)

s = input()
ss = []
for i in range(len(s)-1, -1, -1):
    ss.append(s[i])
    
for i in range(len(s)-1):
    if ss[i] == "6":
        ss[i] = "9"
    elif ss[i] == "9":
        ss[i] = "6"
    
ss = "".join(ss)
print(ss)

#- リスト内包表記も利用したショートコード
# print(input()[::-1].translate(str.maketrans({'6': '9', '9': '6'})))