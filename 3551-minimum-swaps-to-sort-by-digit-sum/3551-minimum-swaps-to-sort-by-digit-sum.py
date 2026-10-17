
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        # Store original indices and sort by digit sum, then number
        arr = sorted(
            [(digit_sum(x), x, i) for i, x in enumerate(nums)]
        )

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
