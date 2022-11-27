"""
BaseQueue abstract data type (base class) definition for
implementing a queue like data types.

CONSTANTS

    DEQUEUE_NIL = 0              # dequeue() was not called
    DEQUEUE_OK = 1               # last dequeue() call completed
    DEQUEUE_ERR = 2              # last dequeue() call was not completed

    GET_VALUE_NIL = 0            # get_value() was not called
    GET_VALUE_OK = 1             # last get_value() call completed successfully
    GET_VALUE_ERR = 2            # storage is empty

CONSTRUCTOR

    __new__(cls) -> new queue instance
        POST-CONDITION:
            - The queue instance has been created.
    __init__(self):
        POST-CONDITION:
            - The queue command statuses are set to corresponding NIL constants.
            - The queue inner storage size is 0

COMMANDS

    enqueue(self, item: object) — Inserts adds the _item_ in the end of the queue.
        POST-CONDITION:
            - The _item_ is added to the end of the queue.

    dequeue(self) — Delete the "head" item from the queue.
        PRE-CONDITION:
            - The queue is not empty.
            - Item removed from head of queue.

    clear(self) — Delete all items from the queue.
        POST-CONDITION:
            - The queue has been cleared of items.

REQUESTS

    __len__(self) -> Count of enqueued items in queue

    get_first(self) — Returns the value of the first item in queue (item from head).
        PRE-CONDITION:
            - The queue is not empty.
            - The first item value has been returned.

STATUS REQUESTS

    get_dequeue_status(self)    -> returns value of DEQUEUE_*
    get_get_value_status(self)  -> returns value of GET_VALUE_*

"""


from abc import ABCMeta, abstractmethod

class BaseQueue(metaclass=ABCMeta):

    DEQUEUE_NIL : int = 0
    DEQUEUE_OK : int = 1
    DEQUEUE_ERR : int = 2

    GET_VALUE_NIL : int = 0
    GET_VALUE_OK : int = 1
    GET_VALUE_ERR : int = 2

    # constructor
    def __new__(cls) -> object:
        new_instance = super().__new__(cls)
        return new_instance

    @abstractmethod
    def __init__(self):
        """
        POST-CONDITION:
            - The queue command statuses are set to corresponding NIL constants.
            - The queue inner storage size is 0
        """
        # self._queue = []

        # self._get_value_status = self.GET_VALUE_NIL
        # self._dequeue_status = self.DEQUEUE_NIL

    @abstractmethod
    def enqueue(self, value: object):
        """
        POST-CONDITION:
            - The _item_ is added to the end of the queue.
        """

    @abstractmethod
    def dequeue(self):
        """
        PRE-CONDITION:
            - The queue is not empty.
            - Item removed from head of queue.
        """

    @abstractmethod
    def clear(self):
        """
        POST-CONDITION:
            - The queue has been cleared of items.
        """
    @abstractmethod
    def __len__(self) -> int:
        return 0

    @abstractmethod
    def get_first(self):
        """
        PRE-CONDITION:
            - The queue is not empty.
            - The first item value has been returned.
        """
    @abstractmethod
    def get_dequeue_status(self) -> int:
        return 0

    @abstractmethod
    def get_get_value_status(self) -> int:
        return 0

class AbstractQueue(BaseQueue):
    ...
