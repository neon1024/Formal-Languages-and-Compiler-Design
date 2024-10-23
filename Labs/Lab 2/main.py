from HashTable import HashTable


def main():
    hash_table = HashTable()

    hash_table[0] = "Alex"
    hash_table[1] = "Teo"
    hash_table[3] = "Alex"
    hash_table[3] = "Lil Bro"

    print(hash_table)

    assert(hash_table[0] == "Alex")
    assert(hash_table[1] == "Teo")
    assert(hash_table[3] == "Lil Bro")

    assert(hash_table.__contains__(3) == True)
    assert(hash_table.__contains__(5) == False)

    for items in hash_table:
        print(items)


if __name__ == "__main__":
    main()
