"""
Specification and implementation of PowerSet abstract data type,
as heir of HashTable.

It uses same constants and requests as HathTable ADT and constructor still the same.

COMMANDS
    put(self, value: object) - Puts __value__ in the PowerSet storage.
        PRE-CONDITION:
            - __value__ does not exist in HashTable storage.
            - There is empty slot in underlying HashTable.
        POST-CONDITION:
            - the __value__ is placed in the underlying HashTable.

"""

from hash_table import HashTable

class PowerSet(HashTable):

    def put(self, value):
        if not self.is_value(value):
            super().put(value)
        else:
            self.status_put = self.PUT_ERR