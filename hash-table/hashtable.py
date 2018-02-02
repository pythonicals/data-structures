class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.count = 0

    def __str__(self):
        return str(self.slots)

    def __contains__(self, item):
        return self.search(item) != -1

    def __len__(self):
        return self.count

    def hash_function(self, key):
        return hash(key) % self.capacity

    def find_slot(self, key):
        slot = self.hash_function(key)
        while self.slots[slot] is not None and self.slots[slot] != key:
            slot = (slot + 1) % self.capacity
        return slot

    def insert(self, key):
        slot = self.find_slot(key)
        if self.slots[slot] != key:
            self.slots[slot] = key
            self.count += 1

    def search(self, key):
        i = self.find_slot(key)
        if self.slots[i] is not None:  
            return i
        return -1
