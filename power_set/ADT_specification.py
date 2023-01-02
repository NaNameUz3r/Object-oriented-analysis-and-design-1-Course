"""
Specification and implementation of PowerSet abstract data type,
as heir of HashTable.

It uses same constants and requests as HathTable ADT and constructor still the same.

COMMANDS
    put(self, value: object) — Puts __value__ in the PowerSet storage.
        PRE-CONDITION:
            - __value__ does not exist in HashTable storage.
            - There is empty slot in underlying HashTable.
        POST-CONDITION:
            - the __value__ is placed in the underlying HashTable.

    intersection(self, another_set: 'PowerSet') — Return intersection PowerSet of actual PowerSet with passed one.

    union(self, another_set: 'PowerSet') — Return union PowerSet of actual PowerSet with passed one.

    difference(self, another_set: 'PowerSet') — Return difference PowerSet between actual PowerSet with passed one.

    is_subset(self, another_set: 'PowerSet') — Return bool of is actual PowerSet is subset of the passed one.

"""

from hash_table import HashTable
from itertools import chain, filterfalse

class PowerSet(HashTable):

    def __iter__(self):
        """ Iterate over entities of set.
        Implemented for map() used in is_subset request.
        """
        yield from filter(None, self._values)

    def put(self, value):
        """
        Overloading of put() to work as PowerSet expected.
        """
        if not self.is_value(value):
            super().put(value)
        else:
            self.status_put = self.PUT_ERR

    # REQUESTS
    def intersection(self, another_set: 'PowerSet') -> 'PowerSet':
        intersection = self.__class__(self.get_capacity())

        for value in filter(self.is_value, another_set):
            intersection.put(value)

        return intersection

    def union(self, another_set: 'PowerSet') -> 'PowerSet':
        total_elements = len(another_set) + len(self)
        capacity = self.get_capacity()
        if total_elements > capacity:
            capacity = total_elements

        union = self.__class__(capacity)

        for value in chain(self, another_set):
            union.put(value)

        return union

    def difference(self, another_set: 'PowerSet') -> 'PowerSet':
        difference = self.__class__(self.get_capacity())

        for value in filterfalse(another_set.is_value, self):
            difference.put(value)

        return difference

    def is_subset(self, another_set: 'PowerSet') -> bool:
        return all(map(another_set.is_value, self))
