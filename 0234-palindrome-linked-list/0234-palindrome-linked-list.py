# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Convert the linked list to a string
        values = []
        while head:
            values.append(str(head.val))
            head = head.next
        
        # Step 2: Check if the string is a palindrome
        string = "".join(values)
        return string == string[::-1]
