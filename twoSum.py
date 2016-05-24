class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

import unittest

sol = Solution()

class TestTwoSum(unittest.TestCase):

    def test_from_leet(self):
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])

if __name__ == '__main__':
    unittest.main()
