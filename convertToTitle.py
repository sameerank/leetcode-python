class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        from collections import deque
        result = deque('')
        while n > 0:
            n -= 1
            rem = n % 26
            new_ord = rem + ord('A')
            result.appendleft(chr(new_ord))
            n -= rem
            n /= 26
        return "".join(list(result))


import unittest

sol = Solution()

class TestConvertToTitle(unittest.TestCase):

    def test_one(self):
        self.assertEqual(sol.convertToTitle(1), 'A')
        self.assertEqual(sol.convertToTitle(2), 'B')
        self.assertEqual(sol.convertToTitle(25), 'Y')
        self.assertEqual(sol.convertToTitle(26), 'Z')

    def test_two(self):
        self.assertEqual(sol.convertToTitle(28), 'AB')
        self.assertEqual(sol.convertToTitle(54), 'BB')

if __name__ == '__main__':
    unittest.main()
