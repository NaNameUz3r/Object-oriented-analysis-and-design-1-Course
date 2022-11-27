from ADT_specification import BaseAbstractLinkedList

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class ParentLinkedList(BaseAbstractLinkedList):

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

    ADD_TAIL_NIL : int = 0
    ADD_TAIL_OK : int = 1
    ADD_TAIL_ERR : int = 2

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

    def __init__(self):
        self.clear()


    def head(self):
        if self._head:
            self._cursor = self._head
            self.status_head = self.HEAD_OK
        else:
            self.status_head = self.HEAD_ERR

    def tail(self):
        if self._tail:
            self._cursor = self._tail
            self.status_tail = self.TAIL_OK
        else:
            self.status_tail = self.TAIL_ERR

    def right(self):
        if self._cursor and self._cursor != self._tail:
            self._cursor = self._cursor.next
            self.status_right = self.RIGHT_OK
        else:
            self.status_right = self.RIGHT_ERR

    def put_right(self, value):
        if self._cursor is None:
            self.status_put_right = self.PUT_RIGHT_ERR
            return
        else:
            new_node = Node(value)
            new_node.prev = self._cursor
            if self._cursor.next:
                self._cursor.next.prev = new_node
                new_node.next = self._cursor.next
            self._cursor.next = new_node
            if self.is_tail():
                self._tail = new_node
            self._size += 1
            self.status_put_right = self.PUT_RIGHT_OK


    def put_left(self, value):
        if self._cursor is None:
            self.status_put_left = self.PUT_LEFT_ERR
            return
        else:
            new_node = Node(value)
            new_node.next = self._cursor
            if self._cursor.prev:
                self._cursor.prev.next = new_node
                new_node.prev = self._cursor.prev
            self._cursor.prev = new_node
            if self.is_head():
                self._head = new_node
            self._size += 1
            self.status_put_left = self.PUT_LEFT_OK

    def remove(self):
        if self._cursor is None:
            self.status_remove = self.REMOVE_ERR
            return
        else:
            if self.get_size() == 1:
                self.clear()
                self.status_remove = self.REMOVE_OK
                return
            if self.is_head():
                self._cursor.next.prev = None
                self._cursor = self._cursor.next
                self._head = self._cursor
            elif self.is_tail():
                self._cursor.prev.next = None
                self._cursor = self._cursor.prev
                self._tail = self._cursor
            elif self._cursor.next and self._cursor.prev:
                self._cursor.prev.next = self._cursor.next
                self._cursor.next.prev = self._cursor.prev
                self._cursor = self._cursor.next

            self._size -= 1
            self.status_remove = self.REMOVE_OK


    def clear(self):
        self._head = None
        self._tail = None
        self._cursor = None
        self._size = 0

        self.status_head = self.HEAD_NIL
        self.status_tail = self.TAIL_NIL
        self.status_right = self.RIGHT_NIL
        self.status_put_right = self.PUT_RIGHT_NIL
        self.status_put_left = self.PUT_LEFT_NIL
        self.status_remove = self.REMOVE_NIL
        self.status_get = self.GET_NIL
        self.status_add_tail = self.ADD_TAIL_NIL
        self.status_replace = self.REPLACE_NIL
        self.status_find = self.FIND_NIL
        self.status_remove_all = self.REMOVE_ALL_NIL


    def add_tail(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        if self._tail:
            self._tail.next = new_node
            new_node.prev = self._tail
        self._tail = new_node
        if not self.is_value():
            self._cursor = self._tail
        self.status_add_tail = self.ADD_TAIL_OK

    def replace(self, value):
        if self.is_value():
            self._cursor.value = value
            self.status_replace = self.REPLACE_OK
        else:
            self.status_replace = self.REPLACE_ERR

    def find(self, value):
        if self.is_value():
            current_node = self._cursor
            while current_node.next:
                current_node = current_node.next
                if current_node.value == value:
                    self._cursor = current_node
                    self.status_find = self.FIND_OK
                    return
        self.status_find = self.FIND_NOT_FOUND

    def remove_all(self, value):
        if not self.is_value():
            self.status_remove_all = self.REMOVE_ALL_ERR
        else:
            self._cursor = self._head
            removed_counter = 0
            self.status_remove_all = self.REMOVE_ALL_ERR
            while True:
                if self.get() == value:
                    self.remove()
                    removed_counter += 1
                    continue
                self.find(value)
                if self.get_find_status() == self.FIND_OK:
                    removed_counter += 1
                    self.remove()
                else:
                    break
            if removed_counter > 0:
                self.status_remove_all = self.REMOVE_ALL_OK


    def get(self):
        if self._cursor:
            self.status_get = self.GET_OK
            return self._cursor.value
        self.status_get = self.GET_ERR

    def get_size(self):
        return self._size

    def is_head(self):
        if self._cursor:
            return self._cursor == self._head
        return False

    def is_tail(self):
        if self._cursor:
            return self._cursor == self._tail
        return False

    def is_value(self):
        self._cursor is not None


    def get_head_status(self):
        return self.status_head

    def get_tail_status(self):
        return self.status_tail

    def get_right_status(self):
        return self.status_right

    def get_put_right_status(self):
        return self.status_put_right

    def get_put_left_status(self):
        return self.status_put_left

    def get_remove_status(self):
        return self.status_remove

    def get_get_status(self):
        return self.status_get

    def get_replace_status(self):
        return self.status_replace

    def get_find_status(self):
        return self.status_find

    def get_remove_all_status(self):
        return self.status_remove_all

    def get_add_tail_status(self):
        return self.status_add_tail


class LinkedList(ParentLinkedList):
    pass

class TwoWayList(ParentLinkedList):

    LEFT_NIL: int = 0
    LEFT_OK: int = 1
    LEFT_ERR: int = 2

    def clear(self):
        super().clear()
        self.status_left = self.LEFT_NIL

    def left(self):
        if self.is_value() and self._cursor != self._head:
            self._cursor = self._cursor.prev
            self.status_left = self.LEFT_OK
        else:
            self.status_left = self.LEFT_ERR

    def get_status_left(self):
        return self.status_left
