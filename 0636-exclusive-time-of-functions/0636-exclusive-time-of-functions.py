class Solution:
    def exclusiveTime(self, n, logs):
        ans = [0] * n
        stack = []
        prev = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev

                stack.append(fid)
                prev = time

            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1

        return ans