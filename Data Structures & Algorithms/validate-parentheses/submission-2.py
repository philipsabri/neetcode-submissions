class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        s = list(s)
        
        while s:
            current = s.pop()
            if current in mappings:
                if not stack:
                    return False
                closing = stack.pop()
                if mappings[current] != closing:
                    return False
            else:
                stack.append(current)
        return len(stack) == 0