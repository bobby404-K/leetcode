class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k - 1 >= n:
                    break
                total += stoneValue[i + k - 1]
                best = max(best, total - dp[(i + k) % 4])
            dp[i % 4] = best
        
        result = dp[0]
        if result > 0:
            return "Alice"
        elif result < 0:
            return "Bob"
        else:
            return "Tie"