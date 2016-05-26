class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

import unittest

sol = Solution()

class TestReverseString(unittest.TestCase):

    def test_example(self):
        self.assertEqual(sol.reverseString("hello"), "olleh")

if __name__ == '__main__':
    unittest.main()
