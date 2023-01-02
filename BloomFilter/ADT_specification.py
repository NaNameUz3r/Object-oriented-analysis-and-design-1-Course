"""
Specification of BloomFilter abstract data type.

CONSTRUCTOR
    __new__(cls) -> new instance
        POST-CONDITION:
            - The new BloomFilter instance was created.
    __init__(self, size: int):
        Initializes the instance of BloomFilter after it's creation.
        POST-CONDITION:
            - BloomFilter size eq to __size__.
COMMANDS
    add(self, value: object) - Puts the __value__ in BloomFilter.
        POST-CONDITION:
            - The __value__ is put with the BloomFilter.

    clear(self) — Delete all mappings from the BloomFilter.
        POST-CONDITION:
            - BloomFilter is cleared.
REQUESTS
    get_size(self) -> the size of the BloomFilter.
    is_value(self, value: object) -> bool is the __value__ matches the filter?
"""

from bitarray import bitarray


class BloomFilter():

    def __init__(self, f_len):
        self.filter_len = f_len
        self.clear()

    def clear(self):
        self.bitarray = bitarray(self.filter_len)
        self.bitarray.setall(0)

    def _hash1(self, str1):
        bithash = 0
        for c in str1:
            bithash += bithash * 17 + ord(c)
        return bithash % self.filter_len

    def _hash2(self, str1):
        bithash = 0
        for c in str1:
            bithash += bithash * 223 + ord(c)
        return bithash % self.filter_len

    def add(self, str1):
        self.bitarray[self._hash1(str1)] = 1
        self.bitarray[self._hash2(str1)] = 1

    def is_value(self, str1):
        return self.bitarray[self._hash1(str1)] and self.bitarray[self._hash2(str1)]