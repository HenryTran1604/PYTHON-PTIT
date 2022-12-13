
adj = [0] * 1001
vis = [False] * 1001
def dfs(i):
    vis[i] = True
    for j in adj[i]:
        if not vis[j]:
            dfs(j)
def memset():
    for i in range(1001):
        adj[i] = list()
if __name__ == '__main__':
    for _ in range(int(input())):
        memset()
        cnt = 0
        n, m, s, t = [int(x) for x in input().split()]
        for i in range(m):
            tmp = [int(x) for x in input().split()]
            adj[tmp[0]].append(tmp[1])
        for i in range(1, n+1):
            if i != s and i != t:
                vis = [False]  * 1001
                vis[i] = True
                dfs(s)
                if not vis[t]:
                    cnt += 1
        print(cnt)
