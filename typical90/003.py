import io
import sys
_INPUT = """\
5
1 2
1 5
3 5
4 5
"""
sys.stdin = io.StringIO(_INPUT)


# DFSでの実装
N = int(input())
# AB = [list(map(int, input().split())) for _ in range(M)]
G = [[] for i in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
    
print(G)
def dfs(s):
    dist = [-1] * N # 初期化
    dist[s] = 0 # 自分自身との距離は0
    st = [s] # スタックを用意
    
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1

    return dist

# 0から最も遠い点を求める
dist0 = dfs(0)
index = dist0.index(max(dist0))
# その点から更に最も遠い点を求め、長さを直径とする
r_dist = dfs(index)
# 直径に1を加えたものが答えとなる
print(max(r_dist) + 1)