class Solution:
    def isValid(self, s: str) -> bool:
        map_parenthese = {"}": "{", ")": "(", "]": "["}
        stack_parenthese = []
        for c in s:
            if c in map_parenthese:
                if not stack_parenthese:
                    return False
                if map_parenthese[c] != stack_parenthese.pop():
                    return False
            else:
                stack_parenthese.append(c)
        return not stack_parenthese