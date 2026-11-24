
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x

                a, b = g, x
                while b:
                    a, b = b, a % b
                g = a

                a, b = l, x
                while b:
                    a, b = b, a % b
                l = (l // a) * x

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans
