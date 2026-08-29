class Solution:
    def buildArray(self, target, n):
        ans = []
        x = 1

        for t in target:
            while x < t:
                ans.append("Push")
                ans.append("Pop")
                x += 1

            ans.append("Push")
            x += 1

        return ans