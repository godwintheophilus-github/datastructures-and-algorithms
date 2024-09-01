class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(5)
stack.push(10)
print(stack.peek())  # Output: 10
print(stack.size())  # Output: 2
stack.pop()
print(stack.size())  # Output: 1

# Common operations:
print("Common operations:")
print("------------------")

print("1. Push:")
stack.push(5)
stack.push(10)
print(stack.items)  # Output: [5, 10]

print("\n2. Pop:")
popped_element = stack.pop()
print(popped_element)  # Output: 10
print(stack.items)  # Output: [5]

print("\n3. Peek:")
top_element = stack.peek()
print(top_element)  # Output: 5
print(stack.items)  # Output: [5]

print("\n4. is_empty:")
print(stack.is_empty())  # Output: False

print("\n5. size:")
print(stack.size())  # Output: 1