class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

# Example usage:
if __name__ == "__main__":
    # Create a singly linked list
    sll = SinglyLinkedList()

    # Append some nodes
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)

    # Display the linked list
    print("Linked List:")
    sll.display()

    # Delete a node
    sll.delete(3)

    # Display the linked list after deletion
    print("Linked List after deleting 3:")
    sll.display()
