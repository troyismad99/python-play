'''
109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the 
depth of the two subtrees of every node never differ by more than 1.

Example 1:
    Input: head = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [0]
    Output: [0]

Example 4:
    Input: head = [1,3]
    Output: [3,1]

Constraints:
    The number of nodes in head is in the range [0, 2 * 104].
    -10^5 <= Node.val <= 10^5
'''
# 

import functools as fn

def print_binary_tree(node, nodeInfo=None, inverted=False, isTop=True):

   # node value string and sub nodes
   stringValue, leftNode, rightNode = nodeInfo(node)

   stringValueWidth  = len(stringValue)

   # recurse to sub nodes to obtain line blocks on left and right
   leftTextBlock     = [] if not leftNode else print_binary_tree(leftNode,nodeInfo,inverted,False)
   rightTextBlock    = [] if not rightNode else print_binary_tree(rightNode,nodeInfo,inverted,False)

   # count common and maximum number of sub node lines
   commonLines       = min(len(leftTextBlock),len(rightTextBlock))
   subLevelLines     = max(len(rightTextBlock),len(leftTextBlock))

   # extend lines on shallower side to get same number of lines on both sides
   leftSubLines      = leftTextBlock  + [""] *  (subLevelLines - len(leftTextBlock))
   rightSubLines     = rightTextBlock + [""] *  (subLevelLines - len(rightTextBlock))

   # compute location of value or link bar for all left and right sub nodes
   #   * left node's value ends at line's width
   #   * right node's value starts after initial spaces
   leftLineWidths    = [ len(line) for line in leftSubLines  ]                            
   rightLineIndents  = [ len(line)-len(line.lstrip(" ")) for line in rightSubLines ]

   # top line value locations, will be used to determine position of current node & link bars
   firstLeftWidth    = (leftLineWidths   + [0])[0]  
   firstRightIndent  = (rightLineIndents + [0])[0] 

   # width of sub node link under node value (i.e. with slashes if any)
   # aims to center link bars under the value if value is wide enough
   # 
   # ValueLine:    v     vv    vvvvvv   vvvvv
   # LinkLine:    / \   /  \    /  \     / \ 
   #
   linkSpacing       = min(stringValueWidth, 2 - stringValueWidth % 2)
   leftLinkBar       = 1 if leftNode  else 0
   rightLinkBar      = 1 if rightNode else 0
   minLinkWidth      = leftLinkBar + linkSpacing + rightLinkBar
   valueOffset       = (stringValueWidth - linkSpacing) // 2

   # find optimal position for right side top node
   #   * must allow room for link bars above and between left and right top nodes
   #   * must not overlap lower level nodes on any given line (allow gap of minSpacing)
   #   * can be offset to the left if lower subNodes of right node 
   #     have no overlap with subNodes of left node                                                                                                                                 
   minSpacing        = 2
   rightNodePosition = fn.reduce(lambda r,i: max(r,i[0] + minSpacing + firstRightIndent - i[1]), \
                                 zip(leftLineWidths,rightLineIndents[0:commonLines]), \
                                 firstLeftWidth + minLinkWidth)

   # extend basic link bars (slashes) with underlines to reach left and right
   # top nodes.  
   #
   #        vvvvv
   #       __/ \__
   #      L       R
   #
   linkExtraWidth    = max(0, rightNodePosition - firstLeftWidth - minLinkWidth )
   rightLinkExtra    = linkExtraWidth // 2
   leftLinkExtra     = linkExtraWidth - rightLinkExtra

   # build value line taking into account left indent and link bar extension (on left side)
   valueIndent       = max(0, firstLeftWidth + leftLinkExtra + leftLinkBar - valueOffset)
   valueLine         = " " * max(0,valueIndent) + stringValue
   slash             = "\\" if inverted else  "/"
   backslash         = "/" if inverted else  "\\"
   uLine             = "¯" if inverted else  "_"

   # build left side of link line
   leftLink          = "" if not leftNode else ( " " * firstLeftWidth + uLine * leftLinkExtra + slash)

   # build right side of link line (includes blank spaces under top node value) 
   rightLinkOffset   = linkSpacing + valueOffset * (1 - leftLinkBar)                      
   rightLink         = "" if not rightNode else ( " " * rightLinkOffset + backslash + uLine * rightLinkExtra )

   # full link line (will be empty if there are no sub nodes)                                                                                                    
   linkLine          = leftLink + rightLink

   # will need to offset left side lines if right side sub nodes extend beyond left margin
   # can happen if left subtree is shorter (in height) than right side subtree                                                
   leftIndentWidth   = max(0,firstRightIndent - rightNodePosition) 
   leftIndent        = " " * leftIndentWidth
   indentedLeftLines = [ (leftIndent if line else "") + line for line in leftSubLines ]

   # compute distance between left and right sublines based on their value position
   # can be negative if leading spaces need to be removed from right side
   mergeOffsets      = [ len(line) for line in indentedLeftLines ]
   mergeOffsets      = [ leftIndentWidth + rightNodePosition - firstRightIndent - w for w in mergeOffsets ]
   mergeOffsets      = [ p if rightSubLines[i] else 0 for i,p in enumerate(mergeOffsets) ]

   # combine left and right lines using computed offsets
   #   * indented left sub lines
   #   * spaces between left and right lines
   #   * right sub line with extra leading blanks removed.
   mergedSubLines    = zip(range(len(mergeOffsets)), mergeOffsets, indentedLeftLines)
   mergedSubLines    = [ (i,p,line + (" " * max(0,p)) )       for i,p,line in mergedSubLines ]
   mergedSubLines    = [ line + rightSubLines[i][max(0,-p):]  for i,p,line in mergedSubLines ]                        

   # Assemble final result combining
   #  * node value string
   #  * link line (if any)
   #  * merged lines from left and right sub trees (if any)
   treeLines = [leftIndent + valueLine] + ( [] if not linkLine else [leftIndent + linkLine] ) + mergedSubLines

   # invert final result if requested
   treeLines = reversed(treeLines) if inverted and isTop else treeLines

   # return intermediate tree lines or print final result
   if isTop: 
       print("\n".join(treeLines))
   else: 
       return treeLines

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printTree(self):
        print_binary_tree(self, lambda n:(str(n.val), n.left, n.right))  

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        #  easy cases
        if not head:
            return head

        if not head.next:
            return TreeNode(head.val)
        
        # find the middle with slow and fast pointers
        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # new root
        newroot = slow.next

        # cut down the left child
        slow.next = None
        root = TreeNode(newroot.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(newroot.next)
        return root

s = Solution()

a = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
b = s.sortedListToBST(a)
b.printTree()

a = ListNode()
b = s.sortedListToBST(a)
b.printTree()

a = ListNode(0)
b = s.sortedListToBST(a)
b.printTree()

a = ListNode(1, ListNode(3))
b = s.sortedListToBST(a)
b.printTree()

