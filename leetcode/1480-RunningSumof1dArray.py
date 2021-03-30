'''
1480. Running Sum of 1d Array

Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]
 

Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
'''

# Runtime: 40 ms, faster than 64.68% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.3 MB, less than 73.07% of Python3 online submissions for Running Sum of 1d Array.

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
         # from itertools import accumulate
         # return list(accumulate(nums))

        # I doubt they were looking for the built in accumulate :)

        total = 0
        results = []

        for i in nums:
            total += i
            results.append(total)
        
        return results

# examples
s = Solution()

print(s.runningSum([1,2,3,4]))
print(s.runningSum([1,1,1,1]))
print(s.runningSum([3,1,2,10,1]))