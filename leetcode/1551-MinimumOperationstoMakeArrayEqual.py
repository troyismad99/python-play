'''
1551. Minimum Operations to Make Array Equal

You have an array arr of length n where 
    arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y 
    where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] 
    (i.e. perform arr[x] -=1 and arr[y] += 1). 

The goal is to make all the elements of the array equal. 
It is guaranteed that all the elements of the array can be made equal using 
some operations.

Given an integer n, the length of the array. Return the minimum number of 
operations needed to make all the elements of arr equal.

Example 1:
    Input: n = 3
    Output: 2
    Explanation: arr = [1, 3, 5]
    First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
    In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
    Input: n = 6
    Output: 9

Constraints:
    1 <= n <= 10^4
'''
# Runtime: 24 ms        Your runtime beats 97.13 % of python3 submissions.
# Memory Usage: 14.3 MB Your memory usage beats 24.88 % of python3 submissions.

class Solution:
    def minOperations(self, n: int) -> int:
        
        # target is always equal to n
        # for odd numbers we make each digit equal to the middle digit
        # 1,3,5,7,9,11,13 <- make everything a 7
        #       - the 5 and 9 are changed in two steps
        #       - the 3 and 11 take 4 steps
        #       - the 1 and 13 take 6 steps
        #       - total 12 steps
        # step count is (n*n-1)//4
        #
        # even n:
        #  1,3,5,7,9,11 <- n is 6, 
        #       - the 5 and 7 take 1 step
        #       - the 3 and 9 take 3 steps
        #       - the 1 and 11 take 5 steps
        #       - total 9 steps
        # step count is (n*n)//4
        #
        # with rounding both formula are the same:
        return n * n // 4



'''
n = 10
arr = []
for i in range(0, n):
    arr.append((2 * i) + 1)
t = sum(arr) // n
# target is always equal to n
'''

# examples
s = Solution()
print(s.minOperations(3))
print(s.minOperations(6))
