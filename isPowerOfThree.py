class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        elif n >= 3:
            n = n / 3.0
            return self.isPowerOfThree(n)
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """

import unittest

sol = Solution()

class TestIsPowerOfThree(unittest.TestCase):

    def test_three(self):
        self.assertEqual(sol.isPowerOfThree(3), True)

    def test_four(self):
        self.assertEqual(sol.isPowerOfThree(4), False)

    def test_nine(self):
        self.assertEqual(sol.isPowerOfThree(9), True)

    def test_eighteen(self):
        self.assertEqual(sol.isPowerOfThree(18), False)

if __name__ == '__main__':
    unittest.main()
