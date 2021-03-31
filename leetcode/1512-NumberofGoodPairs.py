'''
1512. Number of Good Pairs

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.

Example 3:
    Input: nums = [1,2,3]
    Output: 0

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
'''
# Runtime: 28 ms,      faster than 92.15% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.1 MB, less than 90.75% of Python3 online submissions for Number of Good Pairs.

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        # since a good pair has the same number
        # we can simply count the numbers that occur more than once

        result = 0

        # a dictionary of number occurances
        numDictionary = {}

        for n in nums:
            if n in numDictionary:
                result += numDictionary[n] # we match with every previous occurence
                numDictionary[n] += 1
            else:
                # set the count up for next time we encounter n
                numDictionary[n] = 1

        return result


# examples
s = Solution()

print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))
