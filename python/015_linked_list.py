"""Implementation of a LinkedList in Python"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> Node | None:
        if self.length == 0:
            return None
        elif self.length == 1:
            result = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return result
        else:
            result = None
            current_node = self.head
            while current_node is not None:
                if current_node.next == self.tail:
                    result = current_node.next
                    self.tail = current_node
                    self.tail.next = None
                current_node = current_node.next
            self.length -= 1
            return result

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def pop_first(self):
        result = None
        if self.length == 0:
            return result

        result = self.head
        self.head = self.head.next
        if self.length == 1:
            self.tail = None

        self.length -= 1
        return result



ll = LinkedList(2)
ll.append(3)
ll.prepend(1)
ll.print_list()
