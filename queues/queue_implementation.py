from ADT_specification import BaseQueue

class ParentQueue(BaseQueue):

    REMOVE_FRONT_NIL : int = 0
    REMOVE_FRONT_OK : int = 1
    REMOVE_FRONT_ERR : int = 2

    GET_VALUE_NIL : int = 0
    GET_VALUE_OK : int = 1
    GET_VALUE_ERR : int = 2

    def __init__(self):
        self._queue = []
        self._status_remove_front = self.REMOVE_FRONT_NIL
        self._status_get_value = self.GET_VALUE_NIL

    def __len__(self):
        return len(self._queue)

    def add_tail(self, item):
        self._queue.append(item)

    def remove_front(self):
        if self.__len__() < 1:
            self._status_remove_front = self.REMOVE_FRONT_ERR
            return None

        self._queue.pop(0)
        return None

    def clear(self):
        self._queue.clear()

    def get_front(self):
        if self.__len__() < 1:
            self._status_get_value = self.GET_VALUE_ERR
            return None
        return self._queue[0]

    def get_REMOVE_FRONT_status(self):
        return self._status_remove_front

    def get_get_value_status(self):
        return self._status_get_value

class Queue(ParentQueue):
    pass


class Dequeue(ParentQueue):

    REMOVE_TAIL_NIL : int = 0
    REMOVE_TAIL_OK : int = 1
    REMOVE_TAIL_ERR : int = 2

    def __init__(self):
        self._queue = []
        self._status_remove_front = self.REMOVE_FRONT_NIL
        self._status_remove_tail = self.REMOVE_TAIL_NIL
        self._status_get_value = self.GET_VALUE_NIL


    def add_front(self, item):
        """
        POST-CONDITION:
            - The _item_ is added in the head of the dequeue
        """
        self._queue.insert(0, item)

    def remove_tail(self):
        """
        PRE-CONDITION:
            - The queue is not empty.
            - Item removed from end of the queue.
        """
        dequeue_size = self.__len__()
        if dequeue_size < 1:
            self._status_remove_tail = self.REMOVE_TAIL_ERR
            return None
        self._status_remove_tail = self.REMOVE_TAIL_OK
        return self._queue.pop(dequeue_size - 1)
