class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(":")", "[":"]", "{":"}"}
        stack = []

        for char in s:
            if (char == "{" or char == "[" or char == "("):
                stack.append(char)
            else:
                if (len(stack) == 0 or char != matches[stack[-1]]):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
        
