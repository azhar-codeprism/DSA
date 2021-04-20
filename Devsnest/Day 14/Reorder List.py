# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:

        def cut(head):
            sp, fp = head, head.next
            if not fp:
                return None
            while fp.next and fp.next.next:
                sp = sp.next
                fp = fp.next.next
            if fp.next:
                sp = sp.next
            new_half = sp.next
            sp.next = None
            return new_half

        def reverse(head):
            if not head or not head.next:
                return head
            prev, curr, nxt = head, head.next, head.next.next
            prev.next = None
            while nxt:
                curr.next = prev
                prev, curr, nxt = curr, nxt, nxt.next
            curr.next = prev
            return curr

        half = cut(head)
        half = reverse(half)
        p = head
        while p and half:
            h2 = half.next
            half.next = p.next
            p.next = half

            p = p.next.next
            half = h2
        return head
