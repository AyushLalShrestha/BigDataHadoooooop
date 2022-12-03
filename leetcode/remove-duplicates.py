# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_valid_next_node(self, head):
        while True:
            if not head.next:
                break
            if head.val == head.next.val:
                head = head.next
                continue
            else:
                head.next = self.get_valid_next_node(head.next)
                break
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            head = self.get_valid_next_node(head)
        return head
