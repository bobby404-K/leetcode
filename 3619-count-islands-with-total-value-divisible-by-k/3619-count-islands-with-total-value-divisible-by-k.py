
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] == 0 or
                (r, c) in visited):
                return 0

            visited.add((r, c))

            total = grid[r][c]

            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)

            return total

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and (r, c) not in visited:
                    island_sum = dfs(r, c)

                    if island_sum % k == 0:
                        count += 1

        return count
