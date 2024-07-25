class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def count_nodes(self):
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def print_list(self):
        if self.is_empty():
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(f"(Head: {self.head.data})")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def delete_last_node(self):
        if self.is_empty():
            print("Circular Linked List is empty, nothing to delete")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
        prev.next = self.head

    def delete_first_node(self):
        if self.is_empty():
            print("Circular Linked List is empty, nothing to delete")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next

# Example usage:
if __name__ == "__main__":
    # Create a circular linked list
    cll = CircularLinkedList()

    # Insert nodes at the end
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)

    # Insert a node at the front
    cll.insert_at_front(0)

    # Print the circular linked list
    print("Circular Linked List:")
    cll.print_list()

    # Count the number of nodes
    print("Number of nodes in the Circular Linked List:", cll.count_nodes())

    # Delete the last node
    cll.delete_last_node()

    # Print the circular linked list after deleting the last node
    print("Circular Linked List after deleting the last node:")
    cll.print_list()

    # Delete the first node
    cll.delete_first_node()

    # Print the circular linked list after deleting the first node
    print("Circular Linked List after deleting the first node:")
    cll.print_list()
