"""
BaseDynamicArray abstract data type (base class) definition for
implementing a dynamic array data types.

CONSTANTS
    GET_ITEM_NIL = 0                # __getitem__() was not called
    GET_ITEM_OK = 1                 # last __getitem__() call completed
    GET_ITEM_ERR = 2                # __getitem__() was not completed

    INSERT_NIL = 0                 # insert() was not called
    INSERT_OK = 1                  # last insert() call completed
    INSERT_ERR = 2                 # insert() was not completed

    DELETE_NIL = 0                 # delete() was not called
    DELETE_OK = 1                  # last delete() call completed
    DELETE_ERR = 2                 # delete() was not completed

ATTRIBUTES
    INITIAL_CAPACITY: type int
        Initial capacity of the array.
    MINIMAL_CAPACITY: type int
        Treshold for dividing relocations that can not be supressed.
    CAPACITY_MULTIPLIER: type int
        Dynamic array capacity multiplier in case of insertation
        new item in full array.
    CAPACITY_DELIMITER: type int
        The capacity of the dynamic array is divided by the value of this delimiter
        in the case when deleting an element leads to a decrease in the elements of the array less than _DECREASE_CAPACITY_THRESHOLD_.
    DECREASE_CAPACITY_THRESHOLD: type int
        Capacity fill percentage treshold that triggers array relocation to new size
        divided by _CAPACITY_DELIMITER_.
CONSTRUCTOR
    __new__(cls) -> new DynamicArray instance
        POST-CONDITION:
            - The DynamicArray instance with no items has been created.
    __init__(self, max_size: int):
        POST-CONDITION:
            - DynamicArray capacity set to _INITIAL_CAPACITY_.
            - DynamicArray storage is empty.
COMMANDS
    insert(self, i: int, item: object) - Insert _item_ into _i_ position of DynamicArray.
        PRE-CONDITION:
            - _i_ is in DymanicArray bounds ( 0 < i < "DynamicArray items count").
        POST-CONDITION:
            - DynamicArray subsequent items has been shifted forward
            - DynamicArray capacity has been increased by _CAPACITY_MULTIPLIER_ if there
              was no free space for new item.
    delete(self, i: int) - Delete item in _i_-th position.
        PRE-CONDITION:
            - _i_ is in DynamicArray bounds ( o < i <= "DymanicArray items count").
        POST-CONDITION:
            - DynamicArray subsequent items has been shifted forward.
            - DymanicArray capacity nas been decreased by _CAPACITY_DELEMITER_
              if deletion changes arrays size to size that greated than _MINIMAL_CAPACITY_ and less than _DECREASE_CAPACITY_THRESHOLD_.
ADDITIONAL COMMANDS
    append(self, item: object) - Adds _item_ to the DynamicArrays tail.
        POST-CONDITION:
            - An item has been added to the DyamicArray as the last item.
REQUESTS
    __len__(self)     -> returns count of DynamicArray items.
    __getitem__(self) -> returns existing item of the DynamicArray by index pointer.
        PRE-CONDITION:
            - Passed index points to existing item in DynamicArray.
ADDITIONAL REQUESTS
    get_capacity(self) -> returns capacity of the DynamicArray.
STATUS REQUESTS
    get_getitem_status(self) -> returns status of last __getitem__() call.
    get_insert_status(self)  -> returns status of last insert() call.
    get_delete_status(self)  -> returns status of last delete() call.
"""

from abc import ABCMeta, abstractmethod


class _BaseAbstractDynamicArray(metaclass=ABCMeta):

    GET_ITEM_NIL : int = 0
    GET_ITEM_OK : int = 1
    GET_ITEM_ERR : int = 2

    INSERT_NIL : int = 0
    INSERT_OK : int = 1
    INSERT_ERR : int = 2

    DELETE_NIL : int = 0
    DELETE_OK : int = 1
    DELETE_ERR : int = 2

    @property
    @abstractmethod
    def INITIAL_CAPACITY(self) -> int:
        """Initial capacity of the array."""
        return 0

    @property
    @abstractmethod
    def MIN_CAPACITY(self) -> int:
        """Treshold for dividing relocations that can not be supressed."""
        return 0

    @property
    @abstractmethod
    def CAPACITY_MULTIPLIER(self) -> int:
        """Dynamic array capacity multiplier in case of insertation
        new item in full array"""
        return 0

    @property
    @abstractmethod
    def CAPACITY_DELIMITER(self) -> int:
        """
        The capacity of the dynamic array is divided by the value of this delimiter
        in the case when deleting an element leads to a decrease in the elements of the array less than _DECREASE_CAPACITY_THRESHOLD_.
        """
        return 0

    @property
    @abstractmethod
    def DECREASE_CAPACITY_THRESHOLD(self) -> int:
        """
        Capacity fill percentage treshold that triggers array relocation to new size
        divided by _CAPACITY_DELIMITER_.
        """
        return 0

    # CONSTRUCTOR
    def __new__(cls) -> object:
        """
        Create a class instance
        POST-CONDITION: created a new instance with empty storage
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """Initializing the instance after it's been created"""

    # COMMANDS:
    @abstractmethod
    def insert(self, i: int, item):
        """
        Insert _item_ into _i_ position of DynamicArray.
        PRE-CONDITION:
            - _i_ is in DymanicArray bounds ( 0 < i < "DynamicArray items count").
        POST-CONDITION:
            - DynamicArray subsequent items has been shifted forward
            - DynamicArray capacity has been increased by _CAPACITY_MULTIPLIER_ if there
              was no free space for new item.
        """

    @abstractmethod
    def delete(self, i: int):
        """
        Delete item in _i_-th position.
        PRE-CONDITION:
            - _i_ is in DynamicArray bounds ( o < i <= "DymanicArray items count").
        POST-CONDITION:
            - DynamicArray subsequent items has been shifted forward.
            - DymanicArray capacity nas been decreased by _CAPACITY_DELEMITER_
              if deletion changes arrays size to size that greated than _MINIMAL_CAPACITY_ and less than _DECREASE_CAPACITY_THRESHOLD_.
        """

    # additional commands:
    @abstractmethod
    def append(self, item: object):
        """
        Adds _item_ to the DynamicArrays tail.
        POST-CONDITION:
            - An item has been added to the DyamicArray as the last item.
        """

    # requests:
    @abstractmethod
    def __len__(self) -> int:
        """Returns count of DynamicArray items."""
        return 0

    @abstractmethod
    def __getitem__(self, i: int) -> object:
        """
        Returns existing item of the DynamicArray by index pointer.
        PRE-CONDITION:
            - Passed index points to existing item in DynamicArray.
        """
        return None

    # additional requests:
    def get_capacity(self) -> int:
        """Returns capacity of the DynamicArray."""
        return 0

    # command statuses requests:
    @abstractmethod
    def get_getitem_status(self) -> int:
        """Returns status of last __getitem__() call."""
        return 0

    @abstractmethod
    def get_insert_status(self) -> int:
        """Returns status of last insert() call."""
        return 0

    @abstractmethod
    def get_delete_status(self) -> int:
        """Returns status of last delete() call."""
        return 0


class AbstractDynamicArray(_BaseAbstractDynamicArray):
    ...
