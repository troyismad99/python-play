'''
667. Beautiful Arrangement II

Given two integers n and k, you need to construct a list which contains 
n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], 
    then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
    Input: n = 3, k = 1
    Output: [1, 2, 3]
    Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:
    Input: n = 3, k = 2
    Output: [1, 3, 2]
    Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.

Note:
    The n and k are in the range 1 <= k < n <= 10^4.
'''
# Runtime: 40 ms        Your runtime beats 96.55 % of python3 submissions.
# Memory Usage: 15.1 MB Your memory usage beats 82.76 % of python3 submissions.

class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:

        # Interesting problem. I had to read a few times to realize that 
        # k is the count of the deltas between a rearranged n
        result = [0] * n

        a, z = 1, k + 1
        
        # first for loop fils the values in until the required number of deltas are met
        # first delta is k, then k-1, then k-2 ....
        for i in range(k+1):
            if i % 2:
                result[i] = z
                z -= 1
            else:
                result[i] = a
                a += 1
        
        # second loop fills the remaining values to the end
        # these will all be a delta of 1
        for i in range(k+1,n):
            result[i] = i + 1
        
        return result

s = Solution()
print(s.constructArray(3,1))
print(s.constructArray(3,2))

print(s.constructArray(10,5))
print(s.constructArray(20,5))

print(s.constructArray(30,5))
print(s.constructArray(30,25))
