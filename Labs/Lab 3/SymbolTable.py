from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hash_table = HashTable()
        self.__current_free_position = 0

    def add(self, symbol):
        if symbol in self.__hash_table.values():
            return

        self.__hash_table[self.__current_free_position] = symbol
        self.__current_free_position += 1

    def symbols(self):
        return self.__hash_table.values()

    def clear(self):
        self.__hash_table.clear()
        self.__current_free_position = 0

    def __len__(self):
        return len(self.__hash_table)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__hash_table)
