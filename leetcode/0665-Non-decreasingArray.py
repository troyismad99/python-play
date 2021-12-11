'''
665. Non-decreasing Array

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
    n == nums.length
    1 <= n <= 10^4
    -10^5 <= nums[i] <= 10^5
'''
# 

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        
        # the easy ones
        if (len(nums) == 1) or (len(nums) == 2):
            return True

        # track the number of increasing pairs
        count = 0

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:

                 #  we found an increasing pair
                count += 1

                # exit if more than one bad pair
                if count > 1:
                    return False
                
                # fix the bad pair
                if i == 0:
                    # first element is easy
                    # just bump to higher element, no previous elements to check
                    nums[i] = nums[i + 1]

                elif nums[i - 1] <= nums[i + 1]:
                    # if the previous number corrects the bad pair
                    # set the current number to the previous
                    nums[i] = nums[i - 1]

                else:
                    # adjust the following number fix the pattern
                    nums[i + 1] = nums[i]
            
        return True


s = Solution()
assert s.checkPossibility([4,2,3]) == True
assert s.checkPossibility([4,2,1]) == False

assert s.checkPossibility([1,5,3]) == True
assert s.checkPossibility([4,5,3]) == True