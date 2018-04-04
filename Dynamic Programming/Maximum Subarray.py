class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = max_now = nums[0]
        for i in nums[1:]:
            cur_max = max(i, cur_max + i)
            max_now = max(max_now, cur_max)
        return max_now