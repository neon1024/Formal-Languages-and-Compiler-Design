from HashTable import HashTable
from SymbolTable import SymbolTable


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
    print(ht.keys())

    for key in ht.keys():
        print(key)

    st = SymbolTable()

    print(st)

    st.add('a')

    print(st)
    print(len(st))
    for symbol in st.symbols():
        print(symbol)

    st.clear()

    print(st)
    print(len(st))

    st.add('a')
    st.add('b')
    st.add('c')

    print(st)


if __name__ == "__main__":
    main()
