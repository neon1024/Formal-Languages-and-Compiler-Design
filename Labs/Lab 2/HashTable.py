class HashTable(dict):
    DELETED = "DELETED"

    def __init__(self):
        super().__init__()
        self.__key_value = []
        self.__free_position = 0

    def __setitem__(self, key, value):
        if value == HashTable.DELETED:
            raise "[!] Invalid value"

        if self.__free_position >= len(self.__key_value):
            self.__key_value.append(value)
            self.__free_position += 1
        else:
            self.__key_value[self.__free_position] = value

            while self.__free_position < len(self.__key_value) and self.__key_value[self.__free_position] != HashTable.DELETED:
                self.__free_position += 1

    def __repr__(self):
        return str(self)

    # TODO
    def __str__(self):
        pass
