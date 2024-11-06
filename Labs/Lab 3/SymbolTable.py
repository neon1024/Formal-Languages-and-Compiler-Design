from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__hash_table = HashTable()
        self.__index = 0

    def add(self, symbol):
        if symbol in self.__hash_table.values():
            return

        self.__hash_table[symbol] = self.__index
        self.__index += 1

    # TODO combine symbols and positions into a new method to get the data from the ST more easily

    def symbols(self):
        return self.__hash_table.values()

    def positions(self):
        return self.__hash_table.keys()

    def clear(self):
        self.__hash_table.clear()
        self.__index = 0

    def __len__(self):
        return len(self.__hash_table)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__hash_table)
