class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]
        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        seg = [0] * (4 * n)

        def build(node, left, right):
            if left == right:
                u = next(u for u in range(n) if pos[u] == left)
                seg[node] = 1 << (ord(s[u]) - ord('a'))
                return
            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]

        node_at = [0] * n
        for u in range(n):
            node_at[pos[u]] = u

        def build_fast(node, left, right):
            if left == right:
                u = node_at[left]
                seg[node] = 1 << (ord(s[u]) - ord('a'))
                return
            mid = (left + right) // 2
            build_fast(node * 2, left, mid)
            build_fast(node * 2 + 1, mid + 1, right)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]

        def update(node, left, right, idx, value):
            if left == right:
                seg[node] = value
                return
            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, right, idx, value)
            seg[node] = seg[node * 2] ^ seg[node * 2 + 1]

        def query(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                return seg[node]
            mid = (left + right) // 2
            result = 0
            if ql <= mid:
                result ^= query(node * 2, left, mid, ql, qr)
            if qr > mid:
                result ^= query(node * 2 + 1, mid + 1, right, ql, qr)
            return result

        build_fast(1, 0, n - 1)
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(1, 0, n - 1, pos[u], 1 << (ord(c) - ord('a')))
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = 0

                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]:
                        u, v = v, u
                    mask ^= query(1, 0, n - 1, pos[head[u]], pos[u])
                    u = parent[head[u]]

                if depth[u] > depth[v]:
                    u, v = v, u

                mask ^= query(1, 0, n - 1, pos[u], pos[v])
                ans.append(mask & (mask - 1) == 0)

        return ans