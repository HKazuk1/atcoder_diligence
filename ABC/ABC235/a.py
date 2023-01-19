import io
import sys
_INPUT = """\
999
"""
sys.stdin = io.StringIO(_INPUT)

abc = input()
bca = abc[1:] + abc[:1]
cab = abc[2:] + abc[:2]

print(int(abc) + int(bca) + int(cab))