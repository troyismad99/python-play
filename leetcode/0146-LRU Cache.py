"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

# Runtime:        136 ms Your runtime beats 95.74 % of python3 submissions.
# Memory Usage: 77.30 MB Your memory usage beats 93.63 % of python3 submissions.

from typing import Counter, List
from itertools import product
from collections import OrderedDict

class Node:
    def __init__(self, key=0, val=0, prev=None, next=None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class LRUCache_one:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:

        if key in self.nodes:
            node = self.move_node_to_front(key)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.nodes:
            node = self.move_node_to_front(key)
            node.val = value

        else:            
            if len(self.nodes) >= self.capacity:
                # remove oldest
                self.remove_tail()

            # add new node
            n = Node(key,value)
            self.nodes[key] = n
            self.insert_head(n)

    
    def move_node_to_front(self, key):
        result = self.nodes[key]
        self.remove_node(result)
        self.insert_head(result)
        return result

    def remove_tail(self):

        # do we have any nodes?
        if len(self.nodes) == 0: 
            return
        
        # get the tail
        tail_node = self.tail.prev
        
        #remove
        del self.nodes[tail_node.key]
        self.remove_node(tail_node)

    def remove_node(self, node):
        # remove references to this node
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_head(self, node):
        # place this node first
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node

import unittest


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = LRUCache(2)

    def test_ExampleOne(self):
        self.s.put(1, 1)
        self.s.put(2, 2)
        self.assertEqual(self.s.get(1), 1)
        self.s.put(3, 3)        
        self.assertEqual(self.s.get(2), -1)
        self.s.put(4, 4)
        self.assertEqual(self.s.get(1), -1)
        self.assertEqual(self.s.get(3), 3)
        self.assertEqual(self.s.get(4), 4)

unittest.main()
