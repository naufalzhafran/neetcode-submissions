class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for c in s:
            if c in complement:
                if stack and stack[-1] == complement[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        