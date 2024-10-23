class HashTable(dict):
    NOT_DEFINED = None

    def __init__(self):
        super().__init__()
        self.__key_value = []

    def __getitem__(self, key):
        # TODO better logic
        if key < 0:
            raise KeyError

        if not self.__key_value[key]:
            raise KeyError("[!] Key doesn't exist")

        return self.__key_value[key]

    def __setitem__(self, key, value):
        # TODO hashing

        spaces_to_add = len(self.__key_value) - key + 1 if len(self.__key_value) > key else key - len(self.__key_value) + 1

        for _ in range(spaces_to_add):
            self.__key_value.append(HashTable.NOT_DEFINED)

        self.__key_value[key] = value

    def __delitem__(self, key):
        del self.__key_value[key]

    def keys(self):
        keys = []

        for key in range(len(self.__key_value)):
            if self.__key_value[key]:
                keys.append(key)

        return keys

    def __contains__(self, key):
        # TODO better logic
        if key < 0:
            raise KeyError

        return self.__key_value[key] != HashTable.NOT_DEFINED

    def __len__(self):
        defined_values_count = 0

        for key in range(len(self.__key_value)):
            if self.__key_value[key] != HashTable.NOT_DEFINED:
                defined_values_count += 1

        return defined_values_count

    # TODO
    def __iter__(self):
        return self.__key_value.__iter__()

    def __repr__(self):
        return str(self)

    def __str__(self):
        result = ""

        for key in range(len(self.__key_value)):
            if self.__key_value[key]:
                if isinstance(self.__key_value[key], str):
                    result = result + f'{{{key}: "{self.__key_value[key]}"}}, '
                else:
                    result = result + f"{{{key}: {self.__key_value[key]}}}, "

        result = "[" + result[:len(result) - 2] + "]"

        return result
