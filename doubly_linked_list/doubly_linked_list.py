"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def insert_after(self, value):
        main_next = self.next
        self.next = ListNode(value, self, main_next)
        if main_next:
            main_next.prev = self.next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        self.length += 1
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1
        new_tail = ListNode(value, self.tail)
        if self.head is None and self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.next = new_tail
            self.tail.prev = new_tail
            self.tail = new_tail

    """
    Removes the 3List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        removing = self.tail.value
        self.length = 0
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.head.prev
            self.tail.next.delete()
        return removing

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.length -= 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length > 1 and node is not self.tail:
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
        if node is self.head:
            self.head = node.next
        node.delete()

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        if self.head is None:
            return None
        while current_node is not None:
            if current_node > max_value:
                max_value = current_node.value
            current_node = current_node.next

        return max_value
