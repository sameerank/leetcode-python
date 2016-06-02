class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        idx = 0
        res = 0
        while idx < len(s):
            if idx < len(s) - 1 and d[s[idx]] < d[s[idx + 1]]:
                res += d[s[idx + 1]] - d[s[idx]]
                idx += 2
            else:
                res += d[s[idx]]
                idx += 1
        return res

import unittest

sol = Solution()

class TestRomanToInt(unittest.TestCase):

    def test_one(self):
        self.assertEqual(sol.romanToInt("I"), 1)
        self.assertEqual(sol.romanToInt("II"), 2)
        self.assertEqual(sol.romanToInt("III"), 3)

    def test_four(self):
        self.assertEqual(sol.romanToInt("IV"), 4)

    def test_five(self):
        self.assertEqual(sol.romanToInt("V"), 5)

    def test_six(self):
        self.assertEqual(sol.romanToInt("VI"), 6)
        self.assertEqual(sol.romanToInt("VII"), 7)
        self.assertEqual(sol.romanToInt("VIII"), 8)

    def test_nine(self):
        self.assertEqual(sol.romanToInt("IX"), 9)

    def test_ten(self):
        self.assertEqual(sol.romanToInt("X"), 10)

    def test_3999(self):
        self.assertEqual(sol.romanToInt("MMMCMXCIX"), 3999)

if __name__ == '__main__':
    unittest.main()
