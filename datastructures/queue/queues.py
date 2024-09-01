class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
print(queue.peek())  # Output: 5
print(queue.size())  # Output: 2
queue.dequeue()
print(queue.size())  # Output: 1

# Common operations:
print("Common operations:")
print("------------------")

print("1. Enqueue:")
queue.enqueue(5)
queue.enqueue(10)
print(queue.items)  # Output: [5, 10]

print("\n2. Dequeue:")
dequeued_element = queue.dequeue()
print(dequeued_element)  # Output: 5
print(queue.items)  # Output: [10]

print("\n3. Peek:")
front_element = queue.peek()
print(front_element)  # Output: 10
print(queue.items)  # Output: [10]

print("\n4. is_empty:")
print(queue.is_empty())  # Output: False

print("\n5. size:")
print(queue.size())  # Output: 1