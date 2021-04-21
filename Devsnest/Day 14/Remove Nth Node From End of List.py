# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        temp_node = ListNode(0)
        temp_node.next = head
        fp = temp_node
        sp = temp_node

        for i in range(0, n + 1):
            fp = fp.next

        while fp:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return temp_node.next