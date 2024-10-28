from HashTable import HashTable


def test_add():
    hash_table = HashTable()

    assert len(hash_table) == 0

    hash_table["salary"] = 120000
    hash_table["message"] = "Hello, World!"

    assert len(hash_table) == 2

    assert hash_table["salary"] == 120000
    assert hash_table["message"] == "Hello, World!"

    print(hash_table)


def test_contains():
    hash_table = HashTable()

    assert "Car Keys" in hash_table == False

    hash_table["Car Keys"] = "BMW F36"

    assert "Car Keys" in hash_table == True


def test_update():
    hash_table = HashTable()

    hash_table["salary"] = 120000

    assert hash_table["salary"] == 120000

    hash_table["salary"] = 250000

    assert hash_table["salary"] == 250000


def test_delete():
    hash_table = HashTable()

    hash_table["username"] = "aleeex110"

    assert hash_table["username"] == "aleeex110"

    del hash_table["username"]

    assert len(hash_table) == 0


def test_keys():
    hash_table = HashTable()

    assert len(hash_table.keys()) == 0

    hash_table["salary"] = 120000
    hash_table["CEO"] = "Zuck"
    hash_table["e"] = 2.71

    assert len(hash_table.keys()) == 3

    keys = ["salary", "CEO", "e"]

    assert keys == hash_table.keys()


def test_HashTable():
    test_add()
    # test_contains()
    # test_update()  not required?
    # test_delete()
    # test_keys()


def main():
    # test_HashTable()

    # Example usage
    ht = HashTable()
    ht.add("apple")
    ht.add("banana")
    ht.add("cherry")

    print("Hash Table:", ht)
    print("Position of 'banana':", ht.get_position("banana"))
    print("Position of 'cherry':", ht.get_position("cherry"))
    print("Position of 'apple':", ht.get_position("apple"))
    print("Position of 'non-existent key':", ht.get_position("non-existent key"))


if __name__ == "__main__":
    main()
