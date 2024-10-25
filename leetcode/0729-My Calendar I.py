"""
729. My Calendar I

You are implementing a program to use as your calendar. We can add a new event if 
adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection 
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a 
booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully 
without causing a double booking. 
Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
 

Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""

# Runtime:        208 ms Your runtime beats 63.93 % of python3 submissions.
# Memory Usage: 17.43 MB Your memory usage beats 38.59 % of python3 submissions.

from typing import Counter, List
from itertools import product


class MyCalendar:

    def __init__(self):
        self.events = []

    def book_1(self, start: int, end: int) -> bool:

        if len(self.events) != 0:
            for s, e in self.events:  # .sort(key=lambda tup: tup[0]):

                # conflicts
                if start >= s and start < e:
                    return False

                if end > s and end <= e:
                    return False

                if start <= s and end >= e:
                    return False

        self.events.append((start, end))
        return True

    def book(self, start: int, end: int) -> bool:

        for s, e in self.events:
            if end > s and start < e:
                return False
        self.events.append([start, end])
        return True


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = MyCalendar()

    def test_ExampleOne(self):
        self.assertTrue(self.s.book(10, 20))
        self.assertFalse(self.s.book(15, 25))
        self.assertTrue(self.s.book(20, 30))

    def test_ExampleTwo(self):
        self.assertTrue(self.s.book(10, 20))
        self.assertFalse(self.s.book(15, 25))
        self.assertTrue(self.s.book(20, 30))
        self.assertTrue(self.s.book(5, 10))
        self.assertTrue(self.s.book(30, 40))
        self.assertFalse(self.s.book(10, 40))

    def test_ExampleThree(self):
        self.assertTrue(self.s.book(97, 100))
        self.assertTrue(self.s.book(33, 51))
        self.assertFalse(self.s.book(89, 100))
        self.assertFalse(self.s.book(83, 100))
        self.assertTrue(self.s.book(75, 92))
        self.assertFalse(self.s.book(76, 95))
        self.assertTrue(self.s.book(19, 30))
        self.assertTrue(self.s.book(53, 63))
        self.assertFalse(self.s.book(8, 23))
        self.assertFalse(self.s.book(18, 37))
        self.assertFalse(self.s.book(87, 100))
        self.assertFalse(self.s.book(83, 100))
        self.assertFalse(self.s.book(54, 67))
        self.assertFalse(self.s.book(35, 48))
        self.assertFalse(self.s.book(58, 75))
        self.assertFalse(self.s.book(70, 89))
        self.assertFalse(self.s.book(13, 32))
        self.assertFalse(self.s.book(44, 63))
        self.assertFalse(self.s.book(51, 62))
        self.assertTrue(self.s.book(2, 15))


unittest.main()
