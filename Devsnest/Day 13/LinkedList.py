class LinkedList:
    def __init__(self, data="", next=None):
        self.data = data
        self.next = next


head = LinkedList("node1", LinkedList("node2", LinkedList("node3", None)))


def insert_head(head, data):
    pointer = head
    new_node = LinkedList("new_node")
    new_node.next = pointer
    head = new_node
    return head


def insert_last(head, data):
    new_node = LinkedList(data, None)
    if not head:
        return new_node
    pointer = head
    while pointer.next:
        pointer = pointer.next
    pointer.next = new_node
    return head


head = insert_last(head, "new last node")
head = insert_head(head, "new head node")


while head:
    print(head.data)
    head = head.next
