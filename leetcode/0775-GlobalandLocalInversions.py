'''
775. Global and Local Inversions

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of 
    i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of 
    i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:
    Input: A = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:
    Input: A = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions, and 1 local inversion.

Note:
    A will be a permutation of [0, 1, ..., A.length - 1].
    A will have length in range [1, 5000].
    The time limit for this problem has been reduced.
'''
# Runtime: 352 ms     Your runtime beats 47.78 % of python3 submissions.
# Memory Usage: 15 MB Your memory usage beats 44.44 % of python3 submissions.

class Solution:
    def isIdealPermutation(self, A: list[int]) -> bool:
        
        # every local is also a global so we only need to check
        # for global that is not a local
        # locals are always beside each other so once we find a global that 
        # is not with neighboring elements we are False

        currentMax = A[0]

        for i in range(2, len(A)):
            if A[i] < currentMax:
                return False
            currentMax = max(currentMax, A[i-1])

        return True

s = Solution()
print(s.isIdealPermutation([1,0,2]))
print(s.isIdealPermutation([1,2,0]))

