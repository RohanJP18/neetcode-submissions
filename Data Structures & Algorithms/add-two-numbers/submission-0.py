# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
            if not l2:
                val2 = 0
            else:
                val2 = l2.val

            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10
            curr.next = ListNode(total)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
      

    
