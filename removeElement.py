class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val in nums:
            nums.sort()
            i, j = 0, 0
            while nums[i] != val and nums[j] != val:
                i += 1
                j += 1
            while j < len(nums) and nums[j] == val:
                j += 1
            while j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1
            while len(nums) > i:
                nums.pop()
        return len(nums)
