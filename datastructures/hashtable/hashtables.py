# hash_table.py

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def display(self):
        for index, pairs in enumerate(self.table):
            print(f"Index {index}: {pairs}")


def main():
    hash_table = HashTable(10)

    hash_table.insert("apple", 5)
    hash_table.insert("banana", 7)
    hash_table.insert("orange", 3)

    print("Get apple:", hash_table.get("apple"))  # Output: 5
    print("Get banana:", hash_table.get("banana"))  # Output: 7
    print("Get orange:", hash_table.get("orange"))  # Output: 3

    hash_table.delete("banana")

    print("Get banana after deletion:", hash_table.get("banana"))  # Output: None

    print("Hash Table:")
    hash_table.display()


if __name__ == "__main__":
    main()