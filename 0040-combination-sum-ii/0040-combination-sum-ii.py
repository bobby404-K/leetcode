class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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

                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(c)
                backtrack(i + 1, remaining - c)  
                path.pop()

        backtrack(0, target)
        return result