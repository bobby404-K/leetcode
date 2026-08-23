MOD = 10**9 + 7

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        M = max(nums)

        gcd_table = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(M + 1):
                gcd_table[i][j] = gcd(i, j)

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for v in nums:
            new_dp = [row[:] for row in dp]
            for g1 in range(M + 1):
                row = dp[g1]
                for g2 in range(M + 1):
                    c = row[g2]
                    if c == 0:
                        continue
                    ng1 = v if g1 == 0 else gcd_table[g1][v]
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + c) % MOD
                    ng2 = v if g2 == 0 else gcd_table[g2][v]
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + c) % MOD
            dp = new_dp

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans