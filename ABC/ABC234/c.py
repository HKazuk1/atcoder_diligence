import io
import sys
_INPUT = """\
923423423420220108
"""
sys.stdin = io.StringIO(_INPUT)

# print('{:b}'.format(int(input())).replace('1','2'))

K = int(input())
bin_K = str(bin(K)[2:])
print(bin_K.replace('1','2'))