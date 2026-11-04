# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the list
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        # remove the nth node using counter
        counter = 1
        if n == 1:
            head = head.next
        else: 
            prev = None
            curr = head
            
            while curr:
                next = curr.next
                if counter == n:
                    prev.next = curr.next
                    break
                prev = curr
                curr = next
                counter += 1
       
        # reverse it back
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

