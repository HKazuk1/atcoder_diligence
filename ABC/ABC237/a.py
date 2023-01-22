import io
import sys
_INPUT = """\
-9876543210

"""
sys.stdin = io.StringIO(_INPUT)

print("Yes" if -2**31 <= int(input()) < 2**31 else "No")