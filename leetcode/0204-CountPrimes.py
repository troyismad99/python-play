'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0
 
Constraints:
    0 <= n <= 5 * 106

'''
# Runtime: 732 ms       Your runtime beats 62.35 % of python3 submissions.
# Memory Usage: 91.9 MB Your memory usage beats 19.89 % of python3 submissions.

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # create a list of all the values up to n to mark the primes
        s = [True]*n

        # these are not prime
        s[0] = s[1] = False

        # Use Sieve of Eratosthenes to discover the primes
        # Each true value is a prime number. 
        # The loop marks all multiples of the each true value it encounters
        # loop start
            # 2 is true so it is prime, mark every multiple of 2 as false
            # 3 is true so it is prime, mark every multiple of 3 as false
            # 4 marked false, not prime, skip
            # 5 is true so it is prime, mark every multiple of 5 as false
            # 6 marked false, not prime, skip

        # only need to loop up to sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if s[i] == True:
                # list compreshension to assign all at once
                # extract a sublist: s[i*2:n:i]
                # length of the sublist: len(s[i*2:n:i])
                s[i*2:n:i] = [False] * len(s[i*2:n:i]) # from 2p to the end
        return sum(s)


s = Solution()
assert s.countPrimes(10) == 4
assert s.countPrimes(0) == 0
assert s.countPrimes(1) == 0

print(s.countPrimes(99))
