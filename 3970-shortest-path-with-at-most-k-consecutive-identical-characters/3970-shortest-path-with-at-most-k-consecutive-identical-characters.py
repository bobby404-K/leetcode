import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, labels[0], 1)]
        dist = {(0, labels[0], 1): 0}

        while pq:
            cost, u, last, count = heapq.heappop(pq)

            state = (u, last, count)

            if cost != dist.get(state, float('inf')):
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                c = labels[v]
                new_count = count + 1 if c == last else 1

                if new_count > k:
                    continue

                new_cost = cost + w
                new_state = (v, c, new_count)

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost
                    heapq.heappush(pq, (new_cost, v, c, new_count))

        return -1