# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans =  ListNode(0)
        ans.next = head
        left = ans
        right = left.next

        for i in range(n):
            right = right.next

        while(right):
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return ans.next