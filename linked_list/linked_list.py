"""
LinkedList abstract data type implementing a linked list data structure interface.

CONSTANTS
    HEAD_NIL = 0            # head() was not called
    HEAD_OK = 1             # last head() call completed
    HEAD_ERR = 2            # last head() call was not completed

    TAIL_NIL = 0            # tail() was not called
    TAIL_OK = 1             # last tail() call completed successfully
    TAIL_ERR = 2            # storage is empty

    RIGHT_NIL = 0           # right() was not called
    RIGHT_OK = 1            # last right() call completed
    RIGHT_ERR = 2           # last right() call was not completed

    PUT_RIGHT_NIL = 0       # put_right() was not called
    PUT_RIGHT_OK = 1        # last put_right() call completed
    PUT_RIGHT_ERR = 2       # last put_rigth() call was not completed

    PUT_LEFT_NIL = 0        # put_left() was not called yet
    PUT_LEFT_OK = 1         # last put_left() call completed
    PUT_LEFT_ERR = 2        # last put_left() catl was not completed

    REMOVE_NIL = 0          # remove() was not called
    REMOVE_OK = 1           # last remove() call completed
    REMOVE_ERR = 2          # last remove() call was not completed

    GET_NIL = 0             # get() was not called
    GET_OK = 1              # last get() call completed
    GET_ERR = 2             # last get() call was not completed

    REPLACE_NIL = 0         # replace() was not called
    REPLACE_OK = 1          # last replace() call completed
    REPLACE_ERR = 2         # last replace() call was not completed

    FIND_NIL = 0            # find() not called yet
    FIND_OK = 1             # last find() call completed
    FIND_ERR_= 2            # last find() call was not completed

    REMOVE_ALL_NIL = 0      # remove_all() was not called
    REMOVE_ALL_OK = 1       # last remove_all() call completed
    REMOVE_ALL_ERR = 2      # last remove_all() call was not completed

CONSTRUCTOR
    __new__(cls, max_size: int) -> new linked-list instance
        POST-CONDITION:
            - The LinkedList instance with empty storage has been created
    __init__(self, max_size: int):
        POST-CONDITION:
            - Initialized stack storage was limited to *max_size* items amount
COMMANDS

    head(self) # Moves cursor pointer to the first node in the LinkedList.
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The cursor pointer has been moved to the first node in the LinkedList.

    tail(self) # Moves cursor pointer to the last node in the LinkedList.
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The cursor pointer has been moved to the last node in the LinkedList.

    right(self) # Moves cursor pointer to the next node on the right.
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The cursor pointer is not on the last node of LinkedList;
        POST-CONDITION:
            - The cursor pointer was moved to the next node on the right.

    put_right(self, value: object) # Puts a new node with the defined *value* to
                                   # the right of the node pointed to by the cursor.
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The LinkedList Size of the LinkedList is less than *max_size* of this LinkedList.
        POST-CONDITION:
            - A new node with the defined *value* has been put into LinkedList in the right of
              the node pointed to by the cursor.

    put_left(self, value: object) # Puts a new node with th defined *value* to
                                  # the left of the node pointed to by the cursor.
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The LinkedList Size of the LinkedList is less than *max_size* of this LinkedList.
        POST-CONDITION:
            A new node with the defined *value* has been put into LinkedList in the left of
            the node pointed to by the cursor.

    remove(self) # Removes the node pointed by the cursor from the LinkenList storage.
                 # the cursor is moved to the right node of the deleted node if it exists,
                 # otherwise the cursor is moved to the left of the deleted node if it exists.
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITIONS:
            - The node pointed by the cursor has been removed from the LinkedList storage
            - The cursor was set to the right (priority) or left node of the remote node, or released
              if the remote node was the only node in the LinkedList storage.

    clear(self)
        POST-CONDITION:
            - The LinkedList storage is empty.

ADDITIONAL COMMANDS
    add_tail(self, value: object) # Adds a new node with the defined *value*
                                  # to the LinkedList storage as the last node.
        POST-CONDITION:
            - A new node with the defined *value* was added to the LinkedList storage
              as the last node.

    replace(self, value: object) # Changes the value of the storage of the node pointed by the cursor
                                 # to the new defined values.
        PRE-CONDITON:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The node pointed by the cursor contains a new defined *value*.

    find(self, value: object) # Set the cursors pointer to the next node
                              # with the defined *value* relative to the node pointed
                              # by the cursor.
        POST-CONDITION:
            - The cursor pointer has been set to the next node with the defined *value*
              relative to the node previously pointed to by the cursor.

    remove_all(self, value: object) # Removes all nodes with the defined *value*
                                    # from the LinkedList storage.
        POST-CONDITION:
            - All nodes with the defined *value* was removed from the storage.

REQUESTS
    get(self) -> value of the node the cursor on
        PRE-CONDITION:
            - The LinkedList storage is not empty.

    get_size(self) -> number of items in the LinkedList storage

ADDITIONAL REQUESTS
    is_head(self)   -> BOOL is the cursor pointing on the first LinkedList storage item?
    is_tail(self)   -> BOOL is the cursor pointing on the last LinkedLIst storage item?
    is_value(self)  -> BOOL is the cursor is pointint on the any node?

STATUS REQUESTS
    # Return the statuses of the corresponding commands reflecting the result of the last call of this command.

    get_head_status(self)
    get_tail_status(self)
    get_right_status(self)
    get_put_right_status(self)
    get_put_left_status(self)
    get_remove_status(self)
    get_get_status(self)
    get_replace_status(self)
    get_find_status(self)
    get_remove_all_status(self)
"""


from abc import ABCMeta, abstractmethod


class _BaseAbstractLinkedList(metaclass=ABCMeta):

    HEAD_NIL : int = 0
    HEAD_OK : int = 1
    HEAD_ERR : int = 2

    TAIL_NIL : int = 0
    TAIL_OK : int = 1
    TAIL_ERR : int = 2

    RIGHT_NIL : int = 0
    RIGHT_OK : int = 1
    RIGHT_ERR : int = 2

    PUT_RIGHT_NIL : int = 0
    PUT_RIGHT_OK : int = 1
    PUT_RIGHT_ERR : int = 2

    PUT_LEFT_NIL : int = 0
    PUT_LEFT_OK : int = 1
    PUT_LEFT_ERR : int = 2

    REMOVE_NIL : int = 0
    REMOVE_OK : int = 1
    REMOVE_ERR : int = 2

    GET_NIL : int = 0
    GET_OK : int = 1
    GET_ERR : int = 2

    REPLACE_NIL : int = 0
    REPLACE_OK : int = 1
    REPLACE_ERR : int = 2

    FIND_NIL : int = 0
    FIND_OK : int = 1
    FIND_NOT_FOUND : int = 2

    FIND_EMPTY : int = 3

    REMOVE_ALL_NIL : int = 0
    REMOVE_ALL_OK : int = 1
    REMOVE_ALL_ERR : int = 2


    # constructor
    def __new__(cls) -> object:
        """
        POST-CONDITION:
            - The LinkedList instance with empty storage has been created.
        """
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """
        POST-CONDITION:
            - Initialized stack storage was limited to *max_size* items amount
        """

    # commands
    @abstractmethod
    def head(self):
        """
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The cursor pointer has been moved to the first node in the LinkedList.
        """

    @abstractmethod
    def tail(self):
        """
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The cursor pointer has been moved to the last node in the LinkedList.
        """

    @abstractmethod
    def right(self):
        """
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The cursor pointer is not on the last node of LinkedList;
        POST-CONDITION:
            - The cursor pointer was moved to the next node on the right.
        """

    @abstractmethod
    def put_right(self, value: object):
        """
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The LinkedList Size of the LinkedList is less than *max_size* of this LinkedList.
        POST-CONDITION:
            - A new node with the defined *value* has been put into LinkedList in the right of
              the node pointed to by the cursor.
        """

    @abstractmethod
    def put_left(self, value: object):
        """
        PRE-CONDITIONS:
            - The LinkedList storage is not empty.
            - The LinkedList Size of the LinkedList is less than *max_size* of this LinkedList.
        POST-CONDITION:
            A new node with the defined *value* has been put into LinkedList in the left of
            the node pointed to by the cursor.
        """

    @abstractmethod
    def remove(self):
        """
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        POST-CONDITIONS:
            - The node pointed by the cursor has been removed from the LinkedList storage
            - The cursor was set to the right (priority) or left node of the remote node, or released
              if the remote node was the only node in the LinkedList storage.
        """

    @abstractmethod
    def clear(self):
        """
        POST-CONDITION:
            - The LinkedList storage is empty.
        """

    # additional commands:
    @abstractmethod
    def add_tail(self, value: object):
        """
        POST-CONDITION:
            - A new node with the defined *value* was added to the LinkedList storage
              as the last node.
        """

    @abstractmethod
    def replace(self, value: object):
        """
        PRE-CONDITON:
            - The LinkedList storage is not empty.
        POST-CONDITION:
            - The node pointed by the cursor contains a new defined *value*.
        """

    @abstractmethod
    def find(self, value: object):
        """
]        POST-CONDITION:
            - The cursor pointer has been set to the next node with the defined *value*
              relative to the node previously pointed to by the cursor.
        """

    @abstractmethod
    def remove_all(self, value: object):
        """
        POST-CONDITION:
            - All nodes with the defined *value* was removed from the storage.
        """

    # requests:
    @abstractmethod
    def get(self) -> object:
        """
        PRE-CONDITION:
            - The LinkedList storage is not empty.
        """
        return 0

    @abstractmethod
    def get_size(self) -> int:
        return 0

    # additional requests:
    @abstractmethod
    def is_head(self) -> bool:
        return False

    @abstractmethod
    def is_tail(self) -> bool:
        return False

    @abstractmethod
    def is_value(self) -> bool:
        return False

    # command statuses requests:
    @abstractmethod
    def get_head_status(self) -> int:
        return 0

    @abstractmethod
    def get_tail_status(self) -> int:
        return 0

    @abstractmethod
    def get_right_status(self) -> int:
        return 0

    @abstractmethod
    def get_put_right_status(self) -> int:
        return 0

    @abstractmethod
    def get_put_left_status(self) -> int:
        return 0

    @abstractmethod
    def get_remove_status(self) -> int:
        return 0

    @abstractmethod
    def get_get_status(self) -> int:
        return 0

    @abstractmethod
    def get_replace_status(self) -> int:
        return 0

    @abstractmethod
    def get_find_status(self) -> int:
        return 0

    @abstractmethod
    def get_remove_all_status(self) -> int:
        return 0


class AbstractLinkedList(_BaseAbstractLinkedList):
    ...