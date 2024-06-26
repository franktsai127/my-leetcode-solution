class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"}": "{", ")": "(", "]": "["}
        stack = []

        for a in s:
            if a not in bracket_map:
                stack.append(a)
                continue
            if not stack or bracket_map[a] != stack[-1]:
                return False
            stack.pop()
        return not stack
