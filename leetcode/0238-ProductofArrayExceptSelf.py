'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''
# Runtime: 232 ms,     faster than 86.27% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.2 MB, less than 63.14% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = []

        # for each element the solution is 
        # the product of the left subarray product and the right subarray product

        # left side, it is built up as i increases
        product = 1
        for i in range(len(nums)): 
            result.append(product)
            product *= nums[i]

        # work backwards for the right side of each i
        product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= product
            product *= nums[i]

        return result

# examples
s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))
        