'''
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target, 
return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    Note that different sequences are counted as different combinations.

Example 2:
    Input: nums = [9], target = 3
    Output: 0

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? 
How does it change the problem? 
What limitation we need to add to the question to allow negative numbers?
'''
# Runtime: 36 ms        Your runtime beats 89.81 % of python3 submissions.
# Memory Usage: 14.6 MB Your memory usage beats 32.25 % of python3 submissions.

class Solution:
     def combinationSum4(self, nums: list[int], target: int) -> int:

        # Since the order is important this is really a permutation problem not a combination.
        # (1, 1, 2) (1, 2, 1) (2, 1, 1) are three permutations of the same combination

        # dynamic programming with memoisation to save results that have already been calculated

        memo = [1] + [-1] * target
        nums.sort()

        def dfs (target):
            # do we have this one?
            if memo[target] != -1: 
                return memo[target]

            # calculate it
            res = 0
            for i in nums:
                if i <= target:
                    res += dfs(target - i)
                else:
                    # leave when the numbers get bigger than target
                    break 

            memo[target] = res

            return res

        return dfs(target)


s = Solution()
print(s.combinationSum4([1,2,3], 4))
print(s.combinationSum4([1,2,3,4,5,6], 4))
print(s.combinationSum4([9], 3))

