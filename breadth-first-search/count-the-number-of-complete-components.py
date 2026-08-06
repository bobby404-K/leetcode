class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        count = 0

        for i in range(n):
            if visited[i]:
                continue

          
            stack = [i]
            visited[i] = True
            component = []

            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            num_vertices = len(component)
            num_edges = sum(len(adj[node]) for node in component) // 2

            if num_edges == num_vertices * (num_vertices - 1) // 2:
                count += 1

        return count