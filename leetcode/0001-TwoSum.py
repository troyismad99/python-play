'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

'''

# Runtime:        56 ms Your runtime beats 89.32 % of python3 submissions.
# Memory Usage: 15.3 MB Your memory usage beats 53.25 % of python3 submissions.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        map = {}
        
        for i, ii in enumerate(nums):
            if ii not in map: 
                map[ii] = i
            
            x = target - ii

            if x in map and map[x] != i: 
                return [i, map[x]]