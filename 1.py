# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

print(Solution().twoSum([7, 2, 11, 15], 9))
