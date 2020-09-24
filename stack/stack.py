"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # what attributes do we need?
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # creat a new Node
        new_node = Node(value)
        if self.head is None:
            # updat head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set the next node of my new Node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create a new Node
        new_node = Node(value)
        # consider two cases # the LL is empty
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. LL is Not empty
        else:
            # update next_node of out tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # cases to consider?
        # empy list
        if self.head is None:
            return None
        # else, return Value of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # TODO
        # when removing from the tail
        # empy list?
        if self.head is None:
            return None
            # else return value of old head
        else:
            ret_value = self.tail.get_value()
            # list with 1 elements?
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements?
            else:
                # if curren. next node is not the tail
                # asign current to current.next. then you set it to NONE making it the new tail.
                # return the current value after
                current = self.head
                while current.next_node is not self.tail:
                    current = current.next_node
                #
                current.set_next_node(None)
                self.tail = current
            return ret_value

    def contains(self, value):
        # TODO time permitting
        # loop through LL unitl the next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
        # return True
        return False
        #  return False

    def get_max(self):
        # TODO time permitting
        pass


# Below is the array version

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.size

    def push(self, value):
        # return self.storage.append(value)
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
        return self.storage.remove_head()
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop()
