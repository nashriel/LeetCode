# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the dummy head of the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists until both are exhausted
        while l1 or l2 or carry:
            # Get the current values, 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits and carry
            total = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = total // 10
            
            # The current digit is the remainder of total divided by 10
            current.next = ListNode(total % 10)
            
            # Move to the next node in the result list
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the result list starting from the next of dummy_head
        return dummy_head.next




