'''
1720. Decode XORed Array

There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, 
such that encoded[i] = arr[i] XOR arr[i + 1]. 
For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, 
that is the first element of arr, i.e. arr[0].

Return the original array arr. 
It can be proved that the answer exists and is unique.

Example 1:
    Input: encoded = [1,2,3], first = 1
    Output: [1,0,2,1]
    Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

Example 2:
    Input: encoded = [6,2,7,3], first = 4
    Output: [4,2,0,7,4]

Constraints:
    2 <= n <= 104
    encoded.length == n - 1
    0 <= encoded[i] <= 105
    0 <= first <= 105
'''
# Runtime: 224 ms, faster than 77.37% of Python3 online submissions for Decode XORed Array.
# Memory Usage: 15.8 MB, less than 60.40% of Python3 online submissions for Decode XORed Array.

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        
        # XOR refresher:
        # Exclusive or, "must have one or the other but not both"
        # XOR is commutative, order doesn't matter: A^B == B^A
        # The inverse of XOR is XOR:
        #       If we have C = A^B
        #       We can get A or B back if we have the other value:
        #       A = C^B ( or the cumutative B^C )
        #       B = C^A ( or the cumutative A^C )

        # start with the free one!
        result = [first]
        
        for secretCode in encoded:
            # xor the last element with the current encoded
            result.append(result[-1] ^ secretCode)

        return result

# examples
s = Solution()

print(s.decode([1,2,3], 1))
print(s.decode([6,2,7,3], 4))

