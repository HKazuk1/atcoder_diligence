import io
import sys
_INPUT = """\
Q000011Z
"""
sys.stdin = io.StringIO(_INPUT)

s = input()

# sが8文字か判定
if len(s) == 8:
    # s[0]が大文字か判定
    if s[0].isupper():
        # s[7]が大文字か判定
        if s[7].isupper():
            # s[1:7]が数字か判定
            if s[1:7].isdecimal():
                # s[1:7]が100000~999999か判定
                if 100000 <= int(s[1:7]) <= 999999:
                    print("Yes")
                    exit()

print("No")