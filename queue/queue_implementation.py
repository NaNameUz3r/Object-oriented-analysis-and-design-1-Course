from ADT_specification import BaseQueue

class Queue(BaseQueue):

    DEQUEUE_NIL : int = 0
    DEQUEUE_OK : int = 1
    DEQUEUE_ERR : int = 2

    GET_VALUE_NIL : int = 0
    GET_VALUE_OK : int = 1
    GET_VALUE_ERR : int = 2

    def __init__(self):
        self._queue = []
        self._status_dequeue = self.DEQUEUE_NIL
        self._status_get_value = self.GET_VALUE_NIL

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if self.__len__() < 1:
            self._status_dequeue = self.DEQUEUE_ERR
            return None

        self._queue.pop(0)
        return None

    def clear(self):
        self._queue.clear()

    def get_first(self):
        if self.__len__() < 1:
            self._status_get_value = self.GET_VALUE_ERR
            return None
        return self._queue[0]

    def get_dequeue_status(self):
        return self._status_dequeue

    def get_get_value_status(self):
        return self._status_get_value
