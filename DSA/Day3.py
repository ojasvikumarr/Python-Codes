class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        maxi = 0 
        for i, char in enumerate(s) :
            if char == '(':
                stack.append(i)
            else :
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxi = max(maxi , i - stack[-1])
        return maxi 
        