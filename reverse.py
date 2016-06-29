class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_stringified = str(x)
        if x_stringified[0] == '-':
            res = int('-' + x_stringified[1::][::-1])
        else:
            res = int(x_stringified[::-1])
        return 0 if abs(res) > 2147483650 else res

import unittest

sol = Solution()

class TestReverse(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(sol.reverse(1), 1)

    def test_example_two(self):
        self.assertEqual(sol.reverse(123), 321)

    def test_example_three(self):
        self.assertEqual(sol.reverse(-123), -321)

if __name__ == '__main__':
    unittest.main()
