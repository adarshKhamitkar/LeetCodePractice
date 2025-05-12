class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hash_set

if __name__ == "__main__":
    # Example usage
    my_hash_set = MyHashSet()
    my_hash_set.add(1)
    my_hash_set.add(2)
    print(my_hash_set.contains(1))  # True
    print(my_hash_set.contains(3))  # False
    my_hash_set.add(2)
    print(my_hash_set.contains(2))  # True
    my_hash_set.remove(2)
    print(my_hash_set.contains(2))  # False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)