from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self,):
        return self.val

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        last_odd_node = head
        last_even_node = None
        _next = None
        i = 0
        while head:
            if i == 0:
                head = head.next
            elif i == 1:
                last_even_node = head
                head = head.next
            elif i % 2 == 0:
                _next = head.next
                head.next = last_odd_node.next
                last_odd_node.next = head
                last_odd_node = head
                last_even_node.next = _next
                head = _next
            elif head.next:
                last_even_node = head
                head = head.next
            else:
                break

            i += 1

        return start
                
            
            
            