from HashTable import HashTable


class ProgramInternalFormat:
    def __init__(self):
        self.__table = HashTable()

    def add(self, token, position=-1):
        self.__table[token] = position

    def clear(self):
        self.__table.clear()

    def tokens(self):
        return self.__table.keys()

    def positions(self):
        return self.__table.values()

    def __len__(self):
        return len(self.__table)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__table)
