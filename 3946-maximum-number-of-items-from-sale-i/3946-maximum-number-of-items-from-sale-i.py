from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        arr = sorted(
            [(items[i][1], bonus[i] + 1) for i in range(n)],
            reverse=True
        )

        dp = [-1] * (budget + 1)
        dp[0] = 0
        ans = 0
        i = 0

        while i < n:
            p = arr[i][0]
            group = []

            while i < n and arr[i][0] == p:
                group.append(arr[i])
                i += 1

            any_dp = [-1] * (budget + 1)

            for price, value in group:
                for c in range(budget, price - 1, -1):
                    if dp[c - price] != -1:
                        any_dp[c] = max(any_dp[c], dp[c - price] + value)

                    if any_dp[c - price] != -1:
                        any_dp[c] = max(any_dp[c], any_dp[c - price] + value)

            for c in range(budget + 1):
                if any_dp[c] != -1:
                    ans = max(ans, any_dp[c] + (budget - c) // p)

            for price, value in group:
                for c in range(budget, price - 1, -1):
                    if dp[c - price] != -1:
                        dp[c] = max(dp[c], dp[c - price] + value)

        return ans
