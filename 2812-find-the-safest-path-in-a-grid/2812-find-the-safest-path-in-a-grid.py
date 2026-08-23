from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        if dist[0][0] == 0 or dist[n - 1][n - 1] == 0:
            return 0

        safeness = [[-1] * n for _ in range(n)]
        safeness[0][0] = dist[0][0]
        heap = [(-dist[0][0], 0, 0)]

        while heap:
            neg_s, r, c = heapq.heappop(heap)
            s = -neg_s
            if s < safeness[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return s
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    ns = min(s, dist[nr][nc])
                    if ns > safeness[nr][nc]:
                        safeness[nr][nc] = ns
                        heapq.heappush(heap, (-ns, nr, nc))

        return safeness[n - 1][n - 1]