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


def is_prime(number):
    if number < 2:
        return False

    if number != 2 and number % 2 == 0:
        return False

    for div in range(3, number // 2 + 1, 2):
        if number % div == 0:
            return False

    return True

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(25) == False
    assert is_prime(100) == False
    assert is_prime(101) == True

def main():
    # test_HashTable()

    test_is_prime()

    ht = HashTable()
    ht['apple'] = 10
    ht['banana'] = 20
    ht['grape'] = 30

    print(ht)  # Show the current hash table

    print(ht['apple'])  # Output: 10
    print(ht['banana'])  # Output: 20

    ht['apple'] = 50  # Update the value associated with 'apple'
    print(ht['apple'])  # Output: 50

    del ht['banana']  # Remove the 'banana' key-value pair
    print(ht)  # Show the updated hash table

    ht['a'] = 0
    ht['b'] = 1
    ht['c'] = 2
    ht['12'] = 3

    print(ht)


if __name__ == "__main__":
    main()
