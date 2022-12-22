s = list(map(int,input()))

ans = 'Strong'

if len(set(s)) == 1:
  ans = 'Weak'
else:
  for i in range(7):
    if s == [i,i+1,i+2,i+3] and i <=6:
      ans = 'Weak'
    elif s == [7,8,9,0] or s == [8,9,0,1] or s == [9,0,1,2]:
      ans = 'Weak'
print(ans)