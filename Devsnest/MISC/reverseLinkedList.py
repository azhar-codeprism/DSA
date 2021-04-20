class LinkedList:
    def __init__(self, data="", next=None):
        self.data = data
        self.next = next


head = LinkedList("node1", LinkedList("node2", LinkedList("node3", None)))


def reverse(head):
    if not head:
        return
    reverse(head.next)
    print(head.data)


reverse(head)
