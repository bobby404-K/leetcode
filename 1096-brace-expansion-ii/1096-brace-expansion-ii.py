class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def concat(a, b):
            return {x + y for x in a for y in b}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                else:
                    part = {expression[i]}
                    i += 1

                current = concat(current, part)

            result |= current
            return result, i + 1

        result, _ = parse(0)
        return sorted(result)