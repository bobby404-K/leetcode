class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            num %= k
            new_dp = [0] * k

            new_dp[num] += 1

            for r in range(k):
                if dp[r]:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            for r in range(k):
                ans[r] += dp[r]

        return ans