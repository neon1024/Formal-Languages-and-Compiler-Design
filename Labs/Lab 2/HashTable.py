# class HashTable(dict):
#     DELETED = "DELETED"
#
#     def __init__(self):
#         super().__init__()
#         self.__key_value = []
#         self.__free_position = 0
#
#     # def __setitem__(self, key, value):
#     #     if value == HashTable.DELETED:
#     #         raise "[!] Invalid value"
#     #
#     #     if self.__free_position >= len(self.__key_value):
#     #         self.__key_value.append(value)
#     #         self.__free_position += 1
#     #     else:
#     #         self.__key_value[self.__free_position] = value
#     #
#     #         while self.__free_position < len(self.__key_value) and self.__key_value[self.__free_position] != HashTable.DELETED:
#     #             self.__free_position += 1
#
#     def __repr__(self):
#         return str(self)
#
#     # TODO
#     def __str__(self):
#         pass

class HashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash_2(self, key):
        return key % self.capacity

    def hash_1(self, key, index):
        if isinstance(key, str):
            ascii_sum = 0

            for ch in key:
                ascii_sum += ord(ch)

            key = ascii_sum

        return (self.hash_2(key) + index) % self.capacity

    def hash(self, key):
        index = 0

        while index < self.capacity:
            obtained_key = self.hash_1(key, index)

            if self.table[obtained_key] is None:
                return obtained_key

            index += 1

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe(self, hash_index):
        """Linear probing"""
        start_index = hash_index

        while self.table[hash_index] is not None:
            hash_index = (hash_index + 1) % self.capacity

            if hash_index == start_index:  # Table is full
                raise Exception("Hash table is full")

        return hash_index

    def add(self, key):
        # hash_index = self._hash(key)

        # Find the next available slot
        # index = self._probe(hash_index)
        obtained_key = self.hash(key)

        # Store the key with its current position in the table
        # self.table[index] = (key, self.size)
        self.table[obtained_key] = (key, self.size)
        self.size += 1  # Increment the count for the next position

    def get_position(self, key):
        """Retrieve the position of a key."""
        # hash_index = self._hash(key)
        hash_index = self.hash(key)
        start_index = hash_index

        # Use linear probing to search for the key
        while self.table[hash_index] is not None:
            stored_key, position = self.table[hash_index]
            if stored_key == key:
                return position
            hash_index = (hash_index + 1) % self.capacity
            if hash_index == start_index:  # Circled back, key not found
                break
        return None  # Key not found

    def __str__(self):
        """Return the hash table contents for visualization."""
        return str([entry if entry is not None else None for entry in self.table])
