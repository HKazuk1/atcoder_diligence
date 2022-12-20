import io
import sys
_INPUT = """\
3B
HR
2B
2B
"""
sys.stdin = io.StringIO(_INPUT)

S = [input() for i in range(4)]
# cycle hit の場合と比較する
ch = ["2B", "3B", "H", "HR"]

if sorted(S) == ch:
    print("Yes")
else:
    print("No")