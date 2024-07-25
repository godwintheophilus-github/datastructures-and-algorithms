class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, prev_data, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_data:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next
        print(f"{prev_data} not found in the list.")

    def delete_first(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage:
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()

    # Append some nodes
    dll.append(1)
    dll.append(3)
    dll.append(5)

    # Prepend a node
    dll.prepend(0)

    # Insert after a node
    dll.insert_after(1, 2)

    # Display the linked list forward and backward
    print("Doubly Linked List (Forward):")
    dll.display_forward()
    print("Doubly Linked List (Backward):")
    dll.display_backward()

    # Delete the first node
    dll.delete_first()

    # Display the linked list after deleting the first node
    print("Doubly Linked List after deleting the first node (Forward):")
    dll.display_forward()

    # Delete the last node
    dll.delete_last()

    # Display the linked list after deleting the last node
    print("Doubly Linked List after deleting the last node (Forward):")
    dll.display_forward()

    # Delete an intermediate node
    dll.delete_node(2)

    # Display the linked list after deleting an intermediate node
    print("Doubly Linked List after deleting an intermediate node (Forward):")
    dll.display_forward()
