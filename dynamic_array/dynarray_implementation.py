import ctypes
from collections.abc import Iterable

from ADT_specification import (_BaseAbstractDynamicArray, AbstractDynamicArray)



class _BaseDynamicArray(_BaseAbstractDynamicArray):

    INITIAL_CAPACITY = 16
    MIN_CAPACITY = INITIAL_CAPACITY
    CAPACITY_MULTIPLIER = 2
    CAPACITY_DELIMITER = 1.5
    DECREASE_CAPACITY_THRESHOLD = 50

    def __init__(self):
        super().__init__()
        self.__size = 0
        self.__capacity = self.INITIAL_CAPACITY
        self.__array = self.__make_array(self.__capacity)

        self.__get_item_status = self.GET_ITEM_NIL
        self.__insert_status = self.INSERT_NIL
        self.__delete_status = self.DELETE_NIL

    # COMMANDS:
    def insert(self, i: int, item):
        current_size = len(self)
        capacity = self.get_capacity()

        actual_index = self._resolve_index(i)
        precondition_ok = (actual_index == current_size
                                  or self.__is_idx_in_bounds(actual_index))
        if not precondition_ok:
            self.__insert_status = self.INSERT_BOUNDS_ERR

        if precondition_ok:
            new_size = current_size + 1
            following_items = self.__array[actual_index:current_size]
            if new_size > capacity:
                new_capacity = capacity * self.CAPACITY_MULTIPLIER

                previous_items = self.__array[:actual_index]
                items = previous_items + [item] + following_items
                self.__array = self.__make_array(new_capacity, items)
                self.__capacity = new_capacity
            else:
                self.__array[actual_index:new_size] = [item] + following_items

            self.__size = new_size
            self.__insert_status = self.INSERT_OK
        return

    def delete(self, i: int):
        current_size = len(self)
        capacity = self.get_capacity()

        actual_index = self._resolve_index(i)
        precondition_ok = self.__is_idx_in_bounds(actual_index)
        if not precondition_ok:
            self.__delete_status = self.DELETE_ERR

        if precondition_ok:
            new_size = current_size - 1
            new_fill_factor = new_size / capacity * 100
            following_items = self.__array[actual_index + 1:current_size]
            decrease_capacity = (
                    capacity > self.MIN_CAPACITY
                    and new_fill_factor < self.DECREASE_CAPACITY_THRESHOLD)
            if decrease_capacity:
                new_capacity = int(capacity / self.CAPACITY_DELIMITER)
                if new_capacity < self.MIN_CAPACITY:
                    new_capacity = self.MIN_CAPACITY

                previous_items = self.__array[:actual_index]
                items = previous_items + following_items
                self.__array = self.__make_array(new_capacity, items)
                self.__capacity = new_capacity
            else:
                self.__array[actual_index:new_size] = following_items

            self.__size = new_size
            self.__delete_status = self.DELETE_OK
        return

    # ADDITIONAL COMMANDS:
    def append(self, item):
        i = len(self)
        self.insert(i, item)

    # REQUESTS:
    def __len__(self):
        return self.__size

    def __get_item__(self, i: int) -> object:
        item = None
        actual_index = self._resolve_index(i)
        if self.__is_idx_in_bounds(actual_index):
            item = self.__array[actual_index]
            self.__get_item_status = self.GET_ITEM_OK
        else:
            self.__get_item_status = self.GET_ITEM_ERR

        return item

    # ADDITIONAL REQUESTS:
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __make_array(self, capacity: int, elements: Iterable = None) -> ctypes.Array:
        elements = elements or ()
        return (ctypes.py_object * capacity)(*elements)

    def get_capacity(self) -> int:
        return self.__capacity

    def __is_idx_in_bounds(self, i: int) -> bool:
        count = len(self)
        return 0 <= i < count and count > 0

    # resolve_index method for supporting negative indexes for backward insertation
    def _resolve_index(self, i: int) -> int:
        actual_index = i if i >= 0 else len(self) + i
        return actual_index

    # STATUS REQUESTS:
    def get_getitem_status(self) -> int:
        return self.__get_item_status

    def get_insert_status(self) -> int:
        return self.__insert_status

    def get_delete_status(self) -> int:
        return self.__delete_status


class DynamicArray(AbstractDynamicArray, _BaseDynamicArray):
    ...