class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        import sys
        sys.setrecursionlimit(200000)

        n = len(parent)
        adj = [[] for _ in range(n)]

        for i in range(1, n):
            adj[parent[i]].append(i)

        last = [-1] * 26
        new_parent = parent[:]

        def dfs(node):
            c = ord(s[node]) - ord('a')
            prev = last[c]

            if prev != -1:
                new_parent[node] = prev

            last[c] = node

            for child in adj[node]:
                dfs(child)

            last[c] = prev

        dfs(0)

        new_adj = [[] for _ in range(n)]

        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in new_adj[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)

        return ans
