import io
import sys
_INPUT ="""\
tourist
"""
sys.stdin = io.StringIO(_INPUT)

# S = input()

# if S[-1] == 'r':
#     print("er")
# else:
#     print("ist")
    
print("er" if input()[-1] == "r" else "ist")