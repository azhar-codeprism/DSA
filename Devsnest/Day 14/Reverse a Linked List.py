# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, curr, nxt = head, head.next, head.next.next
        prev.next = None
        while nxt:
            curr.next = prev
            prev, curr, nxt = curr, nxt, nxt.next
        curr.next = prev
        return curr