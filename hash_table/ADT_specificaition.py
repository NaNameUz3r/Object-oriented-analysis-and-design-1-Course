"""
Specification and implementation of HashTable abstract data type.
CONSTANTS
    PUT_NIL             # put() was not called yet
    PUT_OK              # last put() call completed
    PUT_ERR             # put() failed with because HashTable is full

    REMOVE_NIL          # remove() was not called yet
    REMOVE_OK           # last remove() call completed
    REMOVE__ERR         # remove() value is not in the HashTable

CONSTRUCTOR
    __new__(cls) -> new instance
        POST-CONDITION:
            - The new HashTable instance was created.
    __init__(self, capacity: int):
        Initializing the instance after it's been created.
        POST-CONDITION:
            - statuses have set to initial constants.
            - max number of values in the HashTable is set to the passed __capacity__ argument value.
            - initial storage of HashTable is empty (values counter is 0).
COMMANDS
    put(self, value: object) - Puts __value__ in the HashTable storage.
        PRE-CONDITION:
            - the HashTable is not full.
            - __value__ does not exist in HashTable storage.
        POST-CONDITION:
            - the __value__ is put in the HashTable.
    remove(self, value: str) - Remove __value__ from the HashTable storage.
        PRE-CONDITION:
            - __value__ exists in the HashTable storage.
        POST-CONDITION:
            - __value__ removed from HashTable storage.
REQUESTS
    __len__(self) -> counter of values in the HashTable.
    _hash_func(self, value: str) -> __value__ slot.
    get_capacity(self) -> maximum HashTable storage capacity.
    is_value(self, value: str) -> is the __value__ in the HashTable -> bool
STATUS REQUESTS
    get_put_status(self) -> status of last put() invoke.
    get_remove_status(self) -> status of last remove() invoke.
"""


class HashTable:

    PUT_NONE = 0
    PUT_OK = 1
    PUT_ERR = 2

    REMOVE_NONE = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._storage = [None] * self._capacity

        self._put_status = self.PUT_NIL
        self._remove_status = self.REMOVE_NIL

    def clear(self):
        self._storage = [None] * self._capacity
        self.size = 0

        self.status_put = self.PUT_NONE
        self.status_remove = self.REMOVE_NONE

    def put(self, value):
        if self.size < self._capacity:
            for slot in self.__seek_slot(value):
                if self._storage[slot] is None:
                    self.status_put = self.PUT_OK
                    self.size += 1
                    self._storage[slot] = value
                    return
            self.status_put = self.PUT_ERR
            raise Exception('Could not find an empty slot')
        else:
            self.status_put = self.PUT_ERR

    def __hash_func(self, value, increment_salt=0):
        return (id(value)+increment_salt) % self._capacity

    def __seek_slot(self, value):
        return (self.__hash_func(value, ind) for ind in range(self._capacity))

    def remove(self, value):
        if self.size > 0:
            for slot in self.__seek_slot(value):
                if self._storage[slot] is None:
                    break
                if self._storage[slot] == value:
                    self.status_remove = self.REMOVE_OK
                    self._storage[slot] = None
                    return
            self.status_put = self.REMOVE_ERR
        else:
            self.status_remove = self.REMOVE_ERR

    def is_value(self, value):
        if self.size > 0:
            for slot in self.__seek_slot(value):
                if  self._storage[slot] == value or self._storage[slot] is None:
                    break
            return self._storage[slot] == value
        else:
            return False

    def get_capacity(self):
        return self._capacity

    def __len__(self):
        return self.size

    def get_put_status(self):
        return self.status_put

    def get_remove_status(self):
        return self.status_remove