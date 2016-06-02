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

import unittest

sol = Solution()

class TestIsValif(unittest.TestCase):

    def test_one(self):
        self.assertEqual(sol.isValid("()"), True)

    def test_two(self):
        self.assertEqual(sol.isValid("()[]{}"), True)

    def test_three(self):
        self.assertEqual(sol.isValid("(]"), False)

    def test_four(self):
        self.assertEqual(sol.isValid("([)]"), False)

if __name__ == '__main__':
    unittest.main()
