class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        NEG_INF = float('-inf')
        d0 = d1 = d2 = 0
        v = stoneValue  
        
        for i in range(n - 1, -1, -1):
            total = v[i]
            best = total - d0
            
            if i + 1 < n:
                total += v[i + 1]
                diff = total - d1
                if diff > best:
                    best = diff
            
            if i + 2 < n:
                total += v[i + 2]
                diff = total - d2
                if diff > best:
                    best = diff
            
            d0, d1, d2 = best, d0, d1
        
        if d0 > 0:
            return "Alice"
        elif d0 < 0:
            return "Bob"
        return "Tie"