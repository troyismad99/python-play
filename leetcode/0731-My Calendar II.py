"""
731. My Calendar II

You are implementing a program to use as your calendar. We can add a new event 
if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection 
(i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents 
a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the 
calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""

# Runtime:        143 ms Your runtime beats 99.43 % of python3 submissions.
# Memory Usage: 17.65 MB Your memory usage beats 21.35 % of python3 submissions.

from typing import Counter, List
from itertools import product


class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:

        # check for a double booking
        for s, e in self.double_booked:
            if end > s and start < e:
                return False

        # add to double booking the part that overlap
        for s, e in self.events:
            if end > s and start < e:
                self.double_booked.append((max(start, s), min(end, e)))

        # add to events list
        self.events.append((start, end))
        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = MyCalendarTwo()

    def test_ExampleOne(self):
        self.assertTrue(self.s.book(10, 20))
        self.assertTrue(self.s.book(50, 60))
        self.assertTrue(self.s.book(10, 40))
        self.assertFalse(self.s.book(5, 15))
        self.assertTrue(self.s.book(5, 10))
        self.assertTrue(self.s.book(25, 55))

    # def test_ExampleTwo(self):
    #     self.assertTrue(self.s.book(10, 20))
    #     self.assertFalse(self.s.book(15, 25))
    #     self.assertTrue(self.s.book(20, 30))
    #     self.assertTrue(self.s.book(5, 10))
    #     self.assertTrue(self.s.book(30, 40))
    #     self.assertFalse(self.s.book(10, 40))

    # def test_ExampleThree(self):
    #     self.assertTrue(self.s.book(97, 100))
    #     self.assertTrue(self.s.book(33, 51))
    #     self.assertFalse(self.s.book(89, 100))
    #     self.assertFalse(self.s.book(83, 100))
    #     self.assertTrue(self.s.book(75, 92))
    #     self.assertFalse(self.s.book(76, 95))
    #     self.assertTrue(self.s.book(19, 30))
    #     self.assertTrue(self.s.book(53, 63))
    #     self.assertFalse(self.s.book(8, 23))
    #     self.assertFalse(self.s.book(18, 37))
    #     self.assertFalse(self.s.book(87, 100))
    #     self.assertFalse(self.s.book(83, 100))
    #     self.assertFalse(self.s.book(54, 67))
    #     self.assertFalse(self.s.book(35, 48))
    #     self.assertFalse(self.s.book(58, 75))
    #     self.assertFalse(self.s.book(70, 89))
    #     self.assertFalse(self.s.book(13, 32))
    #     self.assertFalse(self.s.book(44, 63))
    #     self.assertFalse(self.s.book(51, 62))
    #     self.assertTrue(self.s.book(2, 15))


unittest.main()
