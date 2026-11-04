from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        low = SortedList()
        high = SortedList()

        sum_low = 0
        sum_high = 0

        def rebalance():
            nonlocal sum_low, sum_high

            while len(low) > len(high) + 1:
                val = low.pop()
                sum_low -= val
                high.add(val)
                sum_high += val

            while len(low) < len(high):
                val = high.pop(0)
                sum_high -= val
                low.add(val)
                sum_low += val

        def add(val):
            nonlocal sum_low, sum_high

            if not low or val <= low[-1]:
                low.add(val)
                sum_low += val
            else:
                high.add(val)
                sum_high += val

            rebalance()

        def remove(val):
            nonlocal sum_low, sum_high

            if val in low:
                low.remove(val)
                sum_low -= val
            else:
                high.remove(val)
                sum_high -= val

            rebalance()

        def get_cost():
            median = low[-1]
            return median * len(low) - sum_low + sum_high - median * len(high)

        cost = [0] * (n - x + 1)

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                cost[i - x + 1] = get_cost()

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost[i - x]
                    )

            prev = curr

        return prev[n]

