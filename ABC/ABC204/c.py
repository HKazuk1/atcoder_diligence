import io
import sys
_INPUT = """\
4 4
1 2
2 3
3 4
4 1
"""
sys.stdin = io.StringIO(_INPUT)


from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)

ans = 0
for i in range(N):
    visited = [0]*N
    
    que = deque()
    que.append(i)
    visited[i] = 1
    ans += 1
    
    while len(que) != 0:
        print(que, visited)
        tar = que.popleft()
        for j in G[tar]:
            # 道で繋がって都市が未到達ならキューに追加
            if visited[j] == 0:
                que.append(j)
                visited[j] = 1
                ans += 1


print(ans)