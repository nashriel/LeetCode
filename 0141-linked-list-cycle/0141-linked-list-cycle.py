# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # base case: if the list is empty or has only one node, it can't have a cycle
        if not head or not head.next:
            return False
        slow, fast = head, head   # Initialize slow and fast pointers
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next            # Move slow pointer one step
            fast = fast.next.next       # Move fast pointer two steps
            
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If fast pointer reaches the end of the list, there is no cycle
        return False
