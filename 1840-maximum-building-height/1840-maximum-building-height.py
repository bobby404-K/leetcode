class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions = restrictions + [[1, 0], [n, n - 1]]
        restrictions.sort(key=lambda x: x[0])
        
        cleaned = []
        seen = set()
        for pos, h in restrictions:
            if pos not in seen:
                seen.add(pos)
                cleaned.append([pos, h])
        restrictions = cleaned
        
        m = len(restrictions)
        
        for i in range(1, m):
            prev_pos, prev_h = restrictions[i - 1]
            pos, h = restrictions[i]
            dist = pos - prev_pos
            restrictions[i][1] = min(h, prev_h + dist)
        
        for i in range(m - 2, -1, -1):
            next_pos, next_h = restrictions[i + 1]
            pos, h = restrictions[i]
            dist = next_pos - pos
            restrictions[i][1] = min(h, next_h + dist)
        
        ans = 0
        for i in range(1, m):
            pos1, h1 = restrictions[i - 1]
            pos2, h2 = restrictions[i]
            dist = pos2 - pos1
            peak = (h1 + h2 + dist) // 2
            ans = max(ans, peak, h1, h2)
        
        return ans