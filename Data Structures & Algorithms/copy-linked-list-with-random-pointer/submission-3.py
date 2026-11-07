"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hsh_mp = {None: None}
        curr_old = head
        
        while curr_old:
            copy = Node(curr_old.val)
            hsh_mp[curr_old] = copy
            curr_old = curr_old.next 
            
        curr_old = head
        while curr_old:
            copy = hsh_mp[curr_old]
            copy.next = hsh_mp[curr_old.next]
            copy.random = hsh_mp[curr_old.random]
            curr_old = curr_old.next

        return hsh_mp[head]

