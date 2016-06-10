class Solution(object):
    def isPowerOfFour(self, num):
        if num == 1:
            return True
        elif num >= 4:
            num = num / 4.0
            return self.isPowerOfFour(num)
        else:
            return False
        """
        :type num: int
        :rtype: bool
        """

import unittest

sol = Solution()

class TestIsPowerOfFour(unittest.TestCase):

    def test_three(self):
        self.assertEqual(sol.isPowerOfFour(3), False)

    def test_four(self):
        self.assertEqual(sol.isPowerOfFour(4), True)

    def test_nine(self):
        self.assertEqual(sol.isPowerOfFour(9), False)

    def test_sixteen(self):
        self.assertEqual(sol.isPowerOfFour(16), True)

if __name__ == '__main__':
    unittest.main()
