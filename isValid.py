class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for char in s:
            if char in dictionary:
                stack.append(char)
            elif char in dictionary.values():
                if len(stack) > 0 and char == dictionary[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return stack == []

        
