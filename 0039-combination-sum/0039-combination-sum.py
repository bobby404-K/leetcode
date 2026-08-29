class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break  

                path.append(c)
                backtrack(i, remaining - c)  
                path.pop()

        backtrack(0, target)
        return result