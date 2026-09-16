class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (2 * k + 1)
        dp[0] = 1
        
        for i in range(1, n + k):
            for j in range(min(2 * k, i), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD
        
        return dp[2 * k]