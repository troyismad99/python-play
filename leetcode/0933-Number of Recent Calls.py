"""
933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:
1 <= t <= 10^9
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
"""

# Runtime:         40 ms      your runtime beats 57.72 % of python3 submissions.
# Memory Usage: 21.66 MB Your memory usage beats 82.50 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, deque
from typing import List, Counter

import math


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        min_t = t - 3000

        #  only keep the ping times that in the proper range
        while self.requests and self.requests[0] < min_t:
            self.requests.popleft()
        
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = RecentCounter()

    def test_ExampleOne(self):
        obj = RecentCounter()

        p1 = self.s.ping(1)
        self.assertEqual(p1, 1)

        p1 = self.s.ping(100)
        self.assertEqual(p1, 2)

        p1 = self.s.ping(3001)
        self.assertEqual(p1, 3)

        p1 = self.s.ping(3002)
        self.assertEqual(p1, 3)


unittest.main()
