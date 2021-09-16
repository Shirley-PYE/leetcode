# https://leetcode.com/problems/two-sum/

from functools import cmp_to_key
def cmp(t1, t2):
    return t1[0] - t2[0]

class Solution(object):
    def twoSum(self, nums, target):
        nums = [[nums[i], i] for i in range(0, len(nums))]
        #print(nums)
        nums = sorted(nums, key=cmp_to_key(cmp))
        #print(nums)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i][0] + nums[j][0] == target:
                    return [nums[i][1], nums[j][1]]
                elif nums[i][0] + nums[j][0]  > target:
                    continue

print(Solution().twoSum([7, 2, 11, 15], 9))
