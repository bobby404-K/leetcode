class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        inc = True
        dec = True

        for i in range(1, n):
            if nums[(zero + i) % n] != i:
                inc = False
            if nums[(zero - i) % n] != i:
                dec = False

        ans = n * 2

        if inc:
            ans = min(ans, zero, n - zero + 2)

        if dec:
            ans = min(ans, zero + 2, n - zero)

        return -1 if ans == n * 2 else ans