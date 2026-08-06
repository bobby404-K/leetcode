class Solution:
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        mx = 0
        n = len(nums)
        prefixGcd = [0] * n
        for i in range(n):
            x = nums[i]
            if x > mx:
                mx = x
            prefixGcd[i] = gcd(x, mx)
        prefixGcd.sort()

        total = 0
        i, j = 0, n - 1
        while i < j:
            total += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        return total