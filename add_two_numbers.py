# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode() #initialize a list head
        curr = dummyHead #set the current list to the dummy head
        carry = 0 # this is to carry over the ten's to the next list

        while l1 != None or l2 != None or carry != 0:

            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            columnSum = l1Val + l2Val + carry

            carry = columnSum // 10 #to retrieve the carry from previous operation

            newNode = ListNode(columnSum % 10) #since can only 1 digit

            curr.next = newNode

            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next

