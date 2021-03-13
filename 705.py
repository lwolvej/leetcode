class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [False for _ in range(1000000 + 1)]

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.data[key]
