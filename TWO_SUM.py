class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                
                return [num_to_index[complement], i]
            num_to_index[nums[i]] = i
        
        return []

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.