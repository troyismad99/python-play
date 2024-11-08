"""
649. Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants 
to decide on a change in the Dota2 game. The voting for this change is a round-based 
procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this 
and all the following rounds.

Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. 
The character 'R' and 'D' represent the Radiant party and the Dire party. 
Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. 
This procedure will last until the end of voting. All the senators who have lost their rights 
will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. 
Predict which party will finally announce the victory and change the Dota2 game. 

The output should be "Radiant" or "Dire".

Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 10^4
senate[i] is either 'R' or 'D'.
"""

# Runtime:          7 ms      your runtime beats 97.58 % of python3 submissions.
# Memory Usage: 16.92 MB Your memory usage beats 51.11 % of python3 submissions.

from itertools import product, permutations, combinations, zip_longest
from collections import namedtuple, deque
from typing import List, Counter

import math


class Solution:

    def predictPartyVictory(self, senate: str) -> str:

        radiant = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        n = len(senate)

        while radiant and dire:

            # remove the next senator for each party
            r_index = radiant.popleft()
            d_index = dire.popleft()

            # only the lowest one goes back in the queue
            if r_index < d_index:
                radiant.append(r_index + n)
            else:
                dire.append(d_index + n)

        return "Radiant" if radiant else "Dire"

    def predictPartyVictory_one(self, senate: str) -> str:
        # Runtime:       3178 ms       your runtime beats 5.05 % of python3 submissions.
        # Memory Usage: 16.75 MB Your memory usage beats 79.76 % of python3 submissions.

        q = deque()

        for s in senate:
            q.append(s)

        while True:

            # next senator
            senator = q.popleft()

            # can we Annnounce Victory?
            if q.count(senator) == len(q):
                return "Radiant" if senator == "R" else "Dire"

            # Ban next senator
            if senator == "R":
                q.remove("D")
            else:
                q.remove("R")

            # senator goes to the end of the action line
            q.append(senator)


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ExampleOne(self):
        self.assertEqual(self.s.predictPartyVictory("RD"), "Radiant")

    def test_ExampleTwo(self):
        self.assertEqual(self.s.predictPartyVictory("RDD"), "Dire")

    def test_ExampleThree(self):
        self.assertEqual(self.s.predictPartyVictory("DDRRR"), "Dire")


unittest.main()
