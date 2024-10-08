# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Get values or default to 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate sum including carry
            sum_val = x + y + carry
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            
            # Move to the next nodes if they exist
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next
