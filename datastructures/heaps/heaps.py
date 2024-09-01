# heap.py

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index

        if len(self.heap) > left_child_index and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index

        if len(self.heap) > right_child_index and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index

        if largest_index != index:
            self.heap[largest_index], self.heap[index] = self.heap[index], self.heap[largest_index]
            self._heapify_down(largest_index)

    def display(self):
        print(self.heap)


def main():
    heap = Heap()

    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(4)

    print("Heap after insertion:")
    heap.display()

    print("Deleted element:", heap.delete())
    print("Heap after deletion:")
    heap.display()


if __name__ == "__main__":
    main()