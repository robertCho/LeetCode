# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        
        ans = ListNode(None)
        pointer = ans

        sum = 0
        carry = 0
        while(l1 or l2):
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = int(sum/10)
            pointer.next = ListNode(sum%10)
            pointer = pointer.next
        if(carry>0):
            pointer.next = ListNode(carry)
        
        return ans.next